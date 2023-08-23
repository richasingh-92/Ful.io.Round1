import requests
import urllib.request
from bs4 import BeautifulSoup
import re

def extract_social_links(soup):
    social_links = []
    social_patterns = [r".*facebook.com.*", r".*linkedin.com.*", r".*twitter.com.*", r".*instagram.com.*"]

    for link in soup.find_all("a", href=True):
        for pattern in social_patterns:
            if re.match(pattern, link['href'], re.I):
                social_links.append(link['href'])
                break

    return social_links

def extract_emails(soup):
    emails = []
    response1= urllib.request.urlopen(soup)
    html=response1.read()
    htmlstr=html.decode()
    pattern=re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b',htmlstr)
    for i in pattern:
      emails.append(i)
    return emails

def extract_contacts(soup):
    contacts = []
    response1= urllib.request.urlopen(soup)
    html=response1.read()
    htmlstr=html.decode()
    pattern=re.findall(r'(?:(?:\+\d{1,2}\s?)?(?:\(\d{3}\)|\d{3})[-.\s]?\d{3}[-.\s]?\d{4})',htmlstr)
    for i in pattern:
      contacts.append(i)
    return contacts

def main():
    url = input("Enter a website URL: ")

    response = requests.get(url)
    if response.status_code != 200:
        print("Failed to fetch the webpage.")
        return

    soup = BeautifulSoup(response.content, 'html.parser')

    social_links = extract_social_links(soup)
    emails = extract_emails(url)
    contacts = extract_contacts(url)

    print("Social links -")
    for link in social_links:
        print(link)

    print("Email/s-")
    for email in emails:
        print(email)
    print("Contacts:")
    for contact in contacts:
        print(contact)

if __name__ == "__main__":
    main()
