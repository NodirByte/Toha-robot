import pandas as pd
import openpyxl
from orm_app.models import User  # Import your User model from your Django app
from utils.db_api.connector_db import get_all_users

# Function to export user data to an Excel file
async def export_user_data_to_excel():
    try:
        # Retrieve all users from the database
        users = await get_all_users()
        
        if not users:
            return None
        
        # Initialize an empty list to collect data rows
        data_rows = []
        
        # Iterate over each user and construct data rows
        for user in users:
            data_rows.append({
                "telegram_id": user.telegram_id,
                "channel_status": user.channel_status,
                "created_at": user.created_at.strftime("%Y-%m-%d %H:%M:%S")
            })
        
        # Create a DataFrame from the list of data rows
        df = pd.DataFrame(data_rows)
        
        # Specify the file path for saving the Excel file
        file_path = "media/students.xlsx"
        
        # Write the DataFrame to an Excel file without row indices
        df.to_excel(file_path, index=False)
        print("Exported users data to Excel successfully. ->", file_path)
        
        # Return the file path if export is successful
        return file_path
    
    except Exception as e:
        print(f"Error exporting users data to Excel: {e}")
        return None