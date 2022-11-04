from dotenv import load_dotenv
import uvicorn
from backend.api import server

load_dotenv()

if __name__ == '__main__':
    uvicorn.run(server.app, host='0.0.0.0', port=7000, log_level='info')
