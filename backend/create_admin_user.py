from sqlalchemy.orm import Session
from app.db.session import get_db, SessionLocal
from app.models.user import User
from app.models.learning_history import LearningHistory
from app.core.security import hash_password

def create_admin_user(username: str, password: str):
    db: Session = SessionLocal()
    try:
        existing_user = db.query(User).filter(User.username == username).first()
        if existing_user:
            print(f"Admin user '{username}' already exists.")

            if not existing_user.is_admin:
                existing_user.is_admin = True
                db.commit()
                print(f"User '{username}' has been granted admin privileges.")
            return
        
        admin_user = User(
            username=username,
            hashed_password=hash_password(password=password),
            is_admin=True
        )

        db.add(admin_user)
        db.commit()
        print(f"Admin user '{username}' created successfully.")
    except Exception as e:
        print(f"Error creating admin user: {e}")
    finally:
        db.close()

if __name__ == "__main__":

    create_admin_user("admin", "Batman@2003")