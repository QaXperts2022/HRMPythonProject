import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome()
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

BaseUrl = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
Username = "Admin"
Password = "admin123"

@pytest.fixture(scope="class", autouse=True)
def browser_setup(request):
    chr_options = Options()
    chr_options.add_experimental_option("detach",True)
    request.cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chr_options)

#Pytest Framework 2 Generate Report & Parallel Execution
@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    today = datetime.now()
    report_dir = path("HRMReports", today.strftime("%Y%m%d"))
    report_dir.mkdir(parents=True,exist_ok=True)
    pytest_html = report_dir / f"Report_{'%Y%m%d%H%M'}.html"
    config.option.htmlpath = report_dir
    config.option.self_contained_html = True

def pytest_html_report_title(report):
    report.title = "HRM Test Report"