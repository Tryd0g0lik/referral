# This is a sample Python script.
# from referral.models_more import create_table, engine

import asyncio

from referral.views import app_router


async def main():
    app = await app_router()
    app.run(debug=True)
    return app

if __name__ == "__main__":
    asyncio.run(main())
    
    

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
