from datetime import datetime
from fastapi import FastAPI
from fastapi import FastAPI, HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse


from query_support import *


from create_messages import create_report_file, create_stat_message
from user_id_extractor import get_chat_id
from telegram_direct import TelegramMessanger
from file_writer import create_word_document, delete_document
from analytics import calculate_stats

# Creating an instance of TelegramMessanger
messanger = TelegramMessanger("6859309312:AAFo5rGYbvh8cgW4cnH8OW2JNqNckmgqWy8")

# Creating an instance of fast api
app = FastAPI()

# A post request to add the user details into a google sheet 
@app.post("/user-add/{email}/{full_name}/{user_name}")
def add_user(email: str, full_name: str, user_name: str):
    try:
        # Add user to google sheet
        add_user_to_sheet(email, full_name, user_name)

        return {"user-add successful": True}
    except:
        return {"user-add successful": False}

@app.get("/reports-check/{email}")
def query_user_reports(email: str) -> bool:
    today = datetime.today().strftime('%Y-%m-%d')
    validation_result = validate_presence(email, today)
    return validation_result

@app.get("/reports-get/{user_name}/{email}/{date}")
def get_user_report(user_name: str,email: str, date : str):
    try:
        report_file_path = f"{date}-report.docx"

        # Extract information from google sheets
        google_sheets_data = get_report_record(email, date)

        if google_sheets_data is False:
            raise HTTPException(status_code=404, detail="Date Not Found")

        # Create report message
        report = create_report_file(google_sheets_data)

        # Creating word file
        create_word_document(report, report_file_path)

        # Extract chat id
        chat_id = get_chat_id(user_name)
        
        # Send report
        messanger.send_file(report_file_path, chat_id)

        # Delete report
        delete_document(report_file_path)

        return {"successful": True}
    except: 
        return {"successful": False}

@app.get("/stats-get/{user_name}/{email}/{time_period}/{stat_type}")
def get_user_stats(user_name: str, email: str, time_period: str, stat_type: str):
    try:     
        
        stats_file_path = f"{time_period}-stats.docx"

        # Get statistics, create a formatted message, create a docx file, send it
        stats = calculate_stats(email, time_period, stat_type)
        stat_message = create_stat_message(stats)
        create_word_document(stat_message, stats_file_path)

        # Extract chat id
        chat_id = get_chat_id(user_name)
        
        # Send report
        messanger.send_file(stats_file_path, chat_id)

        # Delete report
        delete_document(stats_file_path)

    
        return {"successful": True}
    except: 
        return {"successful": False}

# A get request to return a list of all unique athlete names for the coach
@app.get("/athletes")
def get_athletes():
    message = get_all_athletes()
    return message

# A get request to return a specific athlete name based on the index
@app.get("/athlete/{index}")
def get_athlete(index: int):
    athlete = get_indexed_athlete(index)
    return athlete





             
             







    

