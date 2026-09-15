# STAMP-UP! Streamlit Demo

## Run locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

Then open the URL shown by Streamlit, normally:

```text
http://localhost:8501
```

## Included
- STAMP-UP! project introduction
- Experience Passport concept
- Explore / Discover / Unlock flow
- Interactive Unlock demo
- Lahug Experience Map
- Lahug Barangay Hall as HOME
- Potential Experience Spots
- Community growth loop
- Partner call-to-action
- Passport cover image

## Lahug Experience Map

The demo includes:
- Lahug Barangay Hall — HOME
- University of the Philippines Cebu
- Waterfront Cebu City Hotel
- Cebu IT Park
- JY Square Mall

The non-HOME locations are presented as **Potential Experience Spots** only and are not represented as confirmed STAMP-UP! partners.

## Recommended next steps
- Add actual partner logos after interviews
- Add QR / NFC interaction
- Add a mock child profile and stamp history
- Add locked / unlocked pins on the map
- Add a language switch if a bilingual version is needed later


## Reward Wish List

Reward data is stored in:

`data/rewards.csv`

You can update the points, tier, reward name, or details directly in that CSV without changing the Streamlit code.

The page includes:
- A points slider
- Locked / unlocked reward cards
- Starter / Active / Achiever / Champion tiers
- An all-rewards table
- A reminder that experiences are the main purpose and rewards are a bonus


## Reward preview images

The Reward Wish List now displays the exact preview images embedded in the supplied Excel workbook.

Images are stored in:

`assets/rewards/`

The image filenames used by each reward are referenced in:

`data/rewards.csv` → `Images`

The 75-point reward contains both the tablet and laptop preview images from the workbook.
