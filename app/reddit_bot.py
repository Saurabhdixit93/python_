from appium import webdriver

def automate_reddit(action, content=None):
    driver = setup_appium()
    if action == "comment":
        post_comment(driver, content)
        return {"status": "Comment posted successfully"}
    else:
        return {"error": "Invalid action"}


def setup_appium():
    # Load Appium server URL from environment variables
    appium_server_url = os.getenv("APPIUM_SERVER_URL", "http://localhost:4723/wd/hub")
    
    # Desired capabilities for the Appium driver
    desired_caps = {
        "platformName": "Android",
        "deviceName": os.getenv("DEVICE_NAME", "emulator-5554"),
        "appPackage": "com.reddit.frontpage",
        "appActivity": "com.reddit.frontpage.MainActivity",
        "noReset": True
    }

    return webdriver.Remote(appium_server_url, desired_caps)

def post_comment(driver, content):
    driver.find_element_by_accessibility_id("Create Post").click()
    driver.find_element_by_id("post_input").send_keys(content)
    driver.find_element_by_accessibility_id("Post").click()
