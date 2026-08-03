from playwright.sync_api import sync_playwright
from axe_playwright_python.sync_playwright import Axe

axe = Axe()

with sync_playwright() as playwright:
    browser = playwright.chromium.launch()
    page = browser.new_page()
    page.goto(r"file:///c%3A/Users/OMNI%20BOOK/OneDrive%20-%20Lancaster%20University/MSc%20Dissertation/MSc%20Project/hitl_agent/outputs/stream_testl/html/leagues.html")
    results = axe.run(page)
    browser.close()

print(f"Found {results.violations_count} violations.")
print(f"Found {results.generate_report()} violations.")