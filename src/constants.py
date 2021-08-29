# url links
LOGIN_URL = "https://sso.wis.ntu.edu.sg/webexe88/owa/sso_login1.asp?p2=http://www.ntu.edu.sg&extra={}"
BOOKING_URL = (
    "http://wis.ntu.edu.sg/pls/webexe88/srce_smain_s.Notice_O?p1={}&p2="
)

# Login x-paths
USERNAME_XPATH = "/html/body/div/div/div[2]/table/tbody/tr/td/form/center[1]/table/tbody/tr/td/table/tbody/tr[2]/td[2]/input"
SELECT_STUDENT_XPATH = "/html/body/div/div/div[2]/table/tbody/tr/td/form/center[1]/table/tbody/tr/td/table/tbody/tr[3]/td[2]/select/option[2]"
LOGIN_XPATH = "/html/body/div/div/div[2]/table/tbody/tr/td/form/center[1]/table/tbody/tr/td/table/tbody/tr[4]/td/input[1]"
PASSWORD_XPATH = "/html/body/div/div/div[2]/table/tbody/tr/td/form/center[1]/table/tbody/tr/td/table/tbody/tr[3]/td[2]/input"
SUBMIT_XPATH = "/html/body/div/div/div[2]/table/tbody/tr/td/form/center[1]/table/tbody/tr/td/table/tbody/tr[5]/td/input[1]"

# Booking landing page x-path
BADMINTON_NORTH_HILL = '//*[@id="top"]/div/section[2]/div/div/p/table/tbody/tr/td[2]/form/ul/li[4]/table[2]/tbody/tr[1]/td/input'

# Badminton court x-paths
BADMINTON_NEXT_WEEK = '//*[@id="top"]/div/section[2]/div/div/p/table/tbody/tr/td[2]/form/table[2]/tbody/tr[{}]/td[{}]/input'
