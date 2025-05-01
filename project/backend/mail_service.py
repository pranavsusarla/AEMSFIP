import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

SMTP_SERVER = 'localhost'
SMTP_PORT = 1025
SENDER_EMAIL = 'no-reply@aemsfip.com'
SENDER_PASSWORD = ''


def sendmailtocompany(comp, job, to):
    msg = MIMEMultipart()

    msg["To"] = comp
    msg["Subject"] = "Match found for this Job Description | AEMFSIP"
    msg["From"] = SENDER_EMAIL

    content = """
<html>
  <body>
    <p>We have found a potential match for your job opening. Here are the details:</p>

    <p><strong>Matched Candidate:</strong> {candidate_name}</p>
    <p><strong>Job Title:</strong> {job_title}</p>
    <p><strong>Description:</strong> {job_description}</p>
    <p><strong>Required Skills:</strong> {job_skills}</p>
    <p><strong>Location:</strong> {job_location}</p>

    <p>We believe this candidate could be a great fit for the role.</p>

    <p>Best Regards,<br>
    AEMSFIP</p>

  </body>
</html>

    """

    email_body = content.format(
        candidate_name=to,
        job_title=job['title'],
        job_description=job['description'],
        job_skills=job['skills'],
        job_location=job['location']
    )

    msg.attach(MIMEText(email_body, 'html'))

    client = smtplib.SMTP(host=SMTP_SERVER, port=SMTP_PORT)

    client.send_message(msg=msg)

    client.quit()

def sendmailtoemployee(to, job):
    msg = MIMEMultipart()

    msg["To"] = to
    msg["Subject"] = "Interview Match found for your Skills | AEMFSIP"
    msg["From"] = SENDER_EMAIL

    content = """
<html>
  <body>
    <h2>New Job Opportunity Matching Your Skills</h2>
    <p>Dear {employee_name},</p>
    <p>We found a job that matches your skillset. Here are the details:</p>

    <p><strong>Job Title:</strong> {job_title}</p>
    <p><strong>Description:</strong> {job_description}</p>
    <p><strong>Required Skills:</strong> {job_skills}</p>
    <p><strong>Location:</strong> {job_location}</p>

    <p>Best Regards,<br>
    AEMSFIP Team</p>

  </body>
</html>

    """

    email_body = content.format(
        employee_name=to,
        job_title=job['title'],
        job_description=job['description'],
        job_skills=job['skills'],
        job_location=job['location']
    )

    msg.attach(MIMEText(email_body, 'html'))

    client = smtplib.SMTP(host=SMTP_SERVER, port=SMTP_PORT)

    client.send_message(msg=msg)

    client.quit()