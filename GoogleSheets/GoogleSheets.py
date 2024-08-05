import gspread
from google.oauth2.service_account import Credentials
from gspread_dataframe import set_with_dataframe
import pandas as pd

class google_sheets:
  """class for google sheets
       https://docs.gspread.org/en/v6.0.1/
       https://google-auth.readthedocs.io/en/master/reference/google.oauth2.service_account.html
       https://gspread-dataframe.readthedocs.io/en/latest/
       """

  def __init__(self, credentials_file, spreadsheet_id, sheet_name):
    """
    my super class that gets all the args that I will need in all the rest of the classes 

    Args:
      credentials_file: The path to the service account credentials JSON file.
      spreadsheet_id: The ID of the Google Sheet.
      sheet_name: sheet name in google sheets.
    """

    self.credentials = Credentials.from_service_account_file(credentials_file)
    self.client = gspread.authorize(self.credentials)
    self.sheet = self.client.open(spreadsheet_name).worksheet(sheet_name)

  def write_to_google_sheet(self, data, start_row=1, start_col=1):
    """
    Writes data to the Google Sheet.

    Args:
      data: The data to write, as a list of lists or a pandas DataFrame.
      start_row: The starting row index for writing data. Defaults to 1.
      start_col: The starting column index for writing data. Defaults to 1.
    """

    if isinstance(data, list):
      self.sheet.update(f"A{start_row}", data)
    elif isinstance(data, pd.DataFrame):
      set_with_dataframe(self.sheet, data, include_index=False, row=start_row, col=start_col)
    else:
      raise ValueError("Invalid data type. Expected list or pandas DataFrame.")

  def read_data_to_dataframe(self):
    """Reads data from the Google Sheet and returns a pandas DataFrame.

    Returns:
      A pandas DataFrame containing the data from the Google Sheet.
    """

    data = self.sheet.get_all_values()
    headers = data[0]
    data = data[1:]
    df = pd.DataFrame(data, columns=headers)
    return df
