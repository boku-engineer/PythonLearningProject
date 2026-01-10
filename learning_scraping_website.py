import os
from pathlib import Path
from playwright.sync_api import sync_playwright


def save_techprep_solution():
    # 1. Automatically find your Mac's Downloads folder
    downloads_path = str(Path.home() / "Downloads")
    output_file = os.path.join(downloads_path, "Rate_Limiter_Solution.pdf")

    target_url = "https://www.techprep.app/system-design/high-level-design/rate-limiter/solution"

    with sync_playwright() as p:
        # Launch browser
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        print(f"Opening {target_url}...")
        page.goto(target_url, wait_until="networkidle")

        # 2. Smart Scroll to trigger lazy-loading content
        print("Scrolling to capture all diagrams and content...")
        page.evaluate("""
            async () => {
                await new Promise((resolve) => {
                    let totalHeight = 0;
                    let distance = 100;
                    let timer = setInterval(() => {
                        let scrollHeight = document.body.scrollHeight;
                        window.scrollBy(0, distance);
                        totalHeight += distance;

                        if(totalHeight >= scrollHeight){
                            clearInterval(timer);
                            resolve();
                        }
                    }, 100);
                });
            }
        """)

        # Wait a moment for any final animations to settle
        page.wait_for_timeout(2000)

        # 3. Generate the PDF
        print(f"Saving PDF to: {output_file}")
        page.pdf(
            path=output_file,
            format="A4",
            print_background=True,
            margin={"top": "20px", "bottom": "20px", "left": "20px", "right": "20px"}
        )

        browser.close()
        print("Done! You can find the file in your Downloads folder.")


if __name__ == "__main__":
    save_techprep_solution()