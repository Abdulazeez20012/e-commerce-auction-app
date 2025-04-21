from app import create_app
from app.services.database import mongo, init_db

app = create_app()
init_db(app)

with app.app_context():
    try:
        ping = mongo.db.command('ping')
        print("✅ MongoDB connection successful:", ping)

        collections = mongo.db.list_collection_names()
        print("📂 Collections:", collections)

        if 'auctions' in collections:
            auctions = list(mongo.db.auctions.find())
            count = mongo.db.auctions.count_documents({})
            print(f"🏷️ Found {count} auctions:")
            for auction in auctions:
                print(f" - {auction.get('title')} (ID: {auction.get('_id')})")
        else:
            print("ℹ️ 'auctions' collection doesn't exist yet")

    except Exception as e:
        print("❌ Error accessing MongoDB:", str(e))