import feedparser
import json

def get_rss_articles(feed_url, source_name, limit=None):
    """
    Fetch and normalize articles from a given RSS feed.
    """
    feed = feedparser.parse(feed_url)

    if feed.bozo:
        raise ValueError(f"Error parsing {source_name} feed: {feed.bozo_exception}")

    articles = []
    for entry in feed.entries[:limit]:
        articles.append({
            "source": source_name,
            "title": getattr(entry, "title", "No Title"),
            "link": getattr(entry, "link", "No Link"),
            "summary": getattr(entry, "summary", "No Summary"),
            "published": getattr(entry, "published", "No Date")
        })
    return articles

if __name__ == "__main__":
    feeds = [
        {
            "url": "https://www.exploit-db.com/rss.xml",
            "name": "ExploitDB"
        },
        {
            "url": "https://nvd.nist.gov/feeds/xml/cve/misc/nvd-rss.xml",
            "name": "NVD"
        },
        {
            "url": "https://feeds.feedburner.com/TheHackersNews",
            "name": "The Hacker News"
        }
    ]

    all_articles = []
    for feed in feeds:
        try:
            articles = get_rss_articles(feed["url"], feed["name"], limit=5)
            all_articles.extend(articles)
        except Exception as e:
            print(f"[!] {e}")

    # Save to JSON
    with open("rss_iocs.json", "w", encoding="utf-8") as f:
        json.dump(all_articles, f, indent=4, ensure_ascii=False)

    print(f"[+] Saved {len(all_articles)} articles to rss_output.json")
