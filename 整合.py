import getpass
from hash_password import hash_password 
from verify_password import verify_password 
print("=== 帳號註冊階段 ===")
reg_password = getpass.getpass("請設定您的註冊密碼: ") 
stored_hash = hash_password(reg_password) 
print(" 註冊成功！ ")

print("=== 帳號登入驗證 ===")

max_attempts = 3
attempts_left = max_attempts

while attempts_left > 0:
    print(f" 您還剩餘 {attempts_left} 次嘗試機會。")
    login_attempt = getpass.getpass("請輸入密碼: ")


    if verify_password(login_attempt, stored_hash):
        print(" 驗證成功！歡迎回來。")
        break
    else:
        attempts_left -= 1


        if attempts_left > 0:
            print(" 密碼錯誤 請再試一次。")
        else:
            print(" 密碼錯誤次數過多")


if attempts_left == 0:
    print(" 請聯絡管理員重設密碼 ")
