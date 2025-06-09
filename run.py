from my_app import app
from my_app import app, db
from my_app.models import Jobs
import datetime

with app.app_context():
    
    # db.create_all()
    
    # job2=Jobs(
    #     job_title="Sr. Software Engineer",
    #     department="Information Technology",
    #     employment_type="Full-time",
    #     min_sal=100000,
    #     max_sal=120000,
    #     start_date=datetime.date(2025, 8, 7),
    #     creation_date =datetime.date(2025, 8, 7),
    #     write_date =datetime.date(2025, 8, 7),
    #     location="Bonifacio Global City Taguig",
    #     description="We are looking for an experienced software developer to join our team. You will be responsible for developing high-quality applications and working with the latest technologies."
    # )
    # db.session.add(job2)
    # db.session.commit()
    
    print(Jobs.query.all())

if __name__ == '__main__':
    app.run(debug=True)
