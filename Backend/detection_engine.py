import re

SCAM_KEYWORDS = ["otp", "bank", "urgent", "click", "password"]


def detect_keywords(text):
    text = text.lower()
    found = []

    for word in SCAM_KEYWORDS:
        if word in text:
            found.append(word)

    return found


def extract_urls(text):
    return re.findall(r"https?://\S+", text)


def compute_score(keywords, urls):
    score = 0

    score += len(keywords) * 10

    if len(urls) > 0:
        score += 20

    return score


def get_level(score):
    if score < 20:
        return "LOW"
    elif score < 50:
        return "MEDIUM"
    else:
        return "HIGH"


def calculate_risk(text):
    keywords = detect_keywords(text)
    urls = extract_urls(text)

    score = compute_score(keywords, urls)
    level = get_level(score)

    return {
        "score": score,
        "level": level,
        "reasons": {
            "keywords": keywords,
            "urls": urls
        }
    }


# TEST CASE
message = "Urgent! click http://bit.ly/login and enter OTP"

result = calculate_risk(message)

print(result)