import os
from sqlalchemy import text
from app import create_app
from app.extensions import db

# Import all models to ensure they are registered with SQLAlchemy
from app.models.auth import Role, User, AuthSession, LoginHistory, AuditLog, SecurityEvent
from app.models.product import Category, Product, ProductImage
from app.models.commerce import Cart, CartItem, Wishlist, WishlistItem, Order, OrderItem, Payment
from app.models.forensics import TransactionLog, FraudDetection, EvidenceCollection

def init_db():
    app = create_app()
    with app.app_context():
        print("Creating database tables if they don't exist...")
        db.create_all()
        print("Database tables created successfully!")

        # Check if we need to seed
        role_count = Role.query.count()
        if role_count == 0:
            print("Database is empty. Seeding data from seeds.sql...")
            seeds_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'database', 'seeds.sql')
            
            if os.path.exists(seeds_path):
                with open(seeds_path, 'r', encoding='utf-8') as f:
                    sql_script = f.read()
                
                # Split the script into separate statements
                statements = sql_script.split(';')
                for statement in statements:
                    if statement.strip():
                        db.session.execute(text(statement))
                
                db.session.commit()
                print("Database seeded successfully!")
            else:
                print(f"Warning: Seed file not found at {seeds_path}")
        else:
            print("Database already contains data. Skipping seed.")

if __name__ == '__main__':
    init_db()
