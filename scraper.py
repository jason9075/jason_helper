import requests
from bs4 import BeautifulSoup

def get_usdtwd_rate() -> str:
    try:
        r = requests.get("https://www.bing.com/search?q=usdtwd")
        soup = BeautifulSoup(r.text, "html.parser")
        result = soup.select_one("div.b_focusTextLarge")
        return result.text.strip() if result else "無法找到匯率資訊"
    except Exception as e:
        return f"發生錯誤: {str(e)}"

# 加入測試用
if __name__ == "__main__":
    print("目前美金兌台幣匯率為：", get_usdtwd_rate())
