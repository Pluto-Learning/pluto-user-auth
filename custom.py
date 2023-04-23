import asyncio
from faker import Faker
from motor.motor_asyncio import AsyncIOMotorDatabase
from src.domain.user.model import User, UserCreate

from src.infastructure.database.mongo import get_client
from src.infastructure.security.password import hash_psw

async def insert_admin_user(user: UserCreate) -> None:
    new_user: User = User(**user.dict())
    db: AsyncIOMotorDatabase = await get_client()
    await db['user'].insert_one(new_user.dict())
    
async def main() -> None:
    fake = Faker()
    
    for _ in range(20):
        username = fake.user_name()
        new_user = UserCreate(
            username=username,
            email=fake.email(),
            password=hash_psw(username),
            pnumber=fake.phone_number(),
            fName=fake.first_name(),
            lName=fake.last_name(),
            address=fake.address().replace('\n', ' '),
        )
        await insert_admin_user(new_user)

if __name__ == "__main__":
    asyncio.run(main())