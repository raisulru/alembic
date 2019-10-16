import uuid
from database.db_session import Session
from database.models import Company, User, Chatbot, DataSet

s = Session()

company_name = 'Google'
company_object = s.query(Company).filter_by(name = company_name).first()

if not company_object:
	company_object = Company(
		company_id=uuid.uuid4(), 
		name='Google', 
		deleted_at=None
	)

s.add(company_object)
s.commit()


users = s.query(User).filter_by(frequency_capping_enabled = True).all()
chatbots = s.query(Chatbot).filter_by(active = False).all()
datasets = s.query(DataSet).all()

for user in users:
    user.company_id = company_object.company_id
    s.add(user)
s.commit()

for chatbot in chatbots:
    chatbot.company_id = company_object.company_id
    s.add(chatbot)
s.commit()

for dataset in datasets:
    dataset.company_id = company_object.company_id
    s.add(dataset)
s.commit()

s.close()