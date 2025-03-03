from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from flask_restful import Api, Resource
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import spacy

from flask_cors import CORS, cross_origin

# Initialize Flask app
app = Flask(__name__)
CORS(app, supports_credentials=True)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///job_matching.db'
app.config['SECRET_KEY'] = 'vnrvjiet project'
app.config['JWT_SECRET_KEY'] = 'JWT_SECRET'
db = SQLAlchemy(app)
api = Api(app)

jwt = JWTManager(app)

# Load spaCy model for NLP
nlp = spacy.load("en_core_web_sm")

# Database Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    type = db.Column(db.String(20), nullable=False)  # 'company' or 'employee'

class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text, nullable=False)
    required_skills = db.Column(db.Text, nullable=False)
    location = db.Column(db.String(120), nullable=False)  # Job location
    salary_range = db.Column(db.String(120), nullable=False)
    company_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

class EmployeeSkill(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    skills = db.Column(db.Text, nullable=False)
    employee_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    employee = db.relationship('User', backref=db.backref('employee_skill', lazy=True))

class JobEmployeeMatch(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    job_id = db.Column(db.Integer, db.ForeignKey('job.id'), nullable=False)  # Foreign key to Job
    employee_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)  # Foreign key to User (employee)

    # Relationships
    job = db.relationship('Job', backref=db.backref('matches', lazy=True))
    employee = db.relationship('User', backref=db.backref('job_matches', lazy=True))

# Helper Functions
def preprocess_text(text):
    """Preprocess text by tokenizing, lemmatizing, and removing stopwords."""
    doc = nlp(text)
    tokens = [token.lemma_.lower() for token in doc if not token.is_stop and not token.is_punct]
    return " ".join(tokens)

def calculate_similarity(job_skills, employee_skills):
    """Calculate cosine similarity between job skills and employee skills."""
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform([job_skills, employee_skills])
    similarity_score = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0]
    return similarity_score

# RESTful Resources
class LoginResource(Resource):
    def post(self):
        """User login endpoint."""
        data = request.json
        email = data.get('email')
        password = data.get('password')

        print(data)

        user = User.query.filter_by(email=email, password=password).first()
        if user:
            user_id = str(user.id)
            print(type(user_id))
            access_token = create_access_token(identity=user_id)
            print('logged in user flask login')
            print('login from backend')
            return {"message": "Login successful", "user_id": user.id, "type": user.type, "token": access_token}, 200
        else:
            return {"message": "Invalid credentials"}, 401

# class LogoutResource(Resource):
#     def post(self):
#         """User logout endpoint."""
#         logout_user()
#         print('logout from backend')
#         return {"message": "Logout successful"}, 200

class JobResource(Resource):
    @jwt_required()
    def post(self):
        """Job posting endpoint."""

        data = request.get_json()
        title = data.get('title')
        description = data.get('description')
        required_skills = data.get('required_skills')
        location = data.get('location')
        salary_range = data.get('salary_range')

        current_user_id = get_jwt_identity()

        print(current_user_id)

        print(data)

        # Validate required fields
        if not all([title, description, required_skills, location, salary_range]):
            return {"message": "Missing required fields"}, 400

        # Create and save the job
        job = Job(
            title=title,
            description=description,
            required_skills=required_skills,
            location=location,
            salary_range=salary_range,
            company_id=current_user_id
        )
        db.session.add(job)
        db.session.commit()

        return {
            "message": "Job posted successfully",
            "job_id": job.id,
            "title": job.title,
            "location": job.location,
            "salary_range": job.salary_range
        }, 201

    @jwt_required()
    def get(self):
        """List all jobs."""
        # List all jobs
        current_user_id = get_jwt_identity()
        jobs = Job.query.filter_by(company_id=current_user_id).all()
        job_list = []
        for job in jobs:
            job_list.append({
                "id": job.id,
                "title": job.title,
                "location": job.location,
                "required_skills": job.required_skills,
                "salary_range": job.salary_range,
                "company_id": job.company_id
            })
        return {"jobs": job_list}, 200

class SkillResource(Resource):
    @jwt_required()
    def post(self):
        data = request.get_json()
        skills = data.get('skills')

        current_user_id = get_jwt_identity()

        try:
            employee_skill = EmployeeSkill.query.filter_by(employee_id=current_user_id).first()

            employee_skill.skills = skills
        except:
            employee_skill = EmployeeSkill(skills=skills, employee_id=current_user_id)
        
        db.session.add(employee_skill)
        db.session.commit()

        return {"message": "Skills uploaded successfully"}, 201

    @jwt_required()
    def get(self):
        current_user_id = get_jwt_identity()
        try:
            user = EmployeeSkill.query.filter_by(employee_id=current_user_id).first()
            if user:
                skills = user.skills
                return jsonify({'skills': skills})
            else:
                return jsonify({'skills': "You have not uploaded your skills yet!"})
        
        except Exception as e:
            print(e)
            return jsonify({'skills': 'An error occured while fetching skills'})

class MatchResource(Resource):
    @jwt_required()
    def get(self, job_id):
        """Job matching endpoint."""
        job = Job.query.get(job_id)
        if not job:
            return {"message": "Job not found"}, 404

        job_skills = preprocess_text(job.required_skills)
        employees = EmployeeSkill.query.all()

        matches = []
        for employee in employees:
            employee_skills = preprocess_text(employee.skills)
            similarity_score = calculate_similarity(job_skills, employee_skills)
            if similarity_score > 0.2:  # Threshold for matching
                matches.append({
                    "employee_name": employee.employee.email,
                    "employee_id": employee.employee_id,
                    "similarity_score": similarity_score,
                    "skills": employee.skills
                })

        # Sort matches by similarity score
        matches.sort(key=lambda x: x['similarity_score'], reverse=True)

        jobemp = JobEmployeeMatch(job_id=job_id, employee_id=matches[0]['employee_id'])

        db.session.add(jobemp)
        db.session.commit()

        return {"matches": matches}, 200

# class UploadResume(Resource):
#     def post(self):
#         print(request.files)
#         # resume = request.files['resume']
#         # resume.save('uploads/resume.pdf')
#         return jsonify({'message': 'saved pdf successfully'})
    
#     def get(self):
#         return jsonify({'message': 'Hi from get'})


# Add resources to API
api.add_resource(LoginResource, '/login')
# api.add_resource(LogoutResource, '/logout')
api.add_resource(JobResource, '/post-job')
api.add_resource(SkillResource, '/upload-skills')
api.add_resource(MatchResource, '/match-employees/<int:job_id>')
# api.add_resource(UploadResume, '/upload-resume')

# @app.after_request
# def after_request(response):
#     print(response.headers)  # Debug: Check if 'Set-Cookie' is present
#     return response

# Run the Flask app
if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create database tables

    app.run(debug=True)