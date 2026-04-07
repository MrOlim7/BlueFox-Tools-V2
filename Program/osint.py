from .legacy_tools import (
    domain_osint,
    email_osint,
    google_dork_generator,
    haveibeenpwned,
    image_metadata,
    phone_osint,
    shodan_search,
    social_media_lookup,
    subdomain_finder,
    tech_stack_detector,
    username_lookup,
    virustotal_check,
    wayback_machine,
)

TOOLS = [
    ("Social Media Lookup", social_media_lookup),
    ("Username Search (50+ sites)", username_lookup),
    ("Email OSINT", email_osint),
    ("Phone Number OSINT", phone_osint),
    ("Domain OSINT (Full)", domain_osint),
    ("Subdomain Finder", subdomain_finder),
    ("Google Dork Generator", google_dork_generator),
    ("Wayback Machine", wayback_machine),
    ("Breach / Leak Check", haveibeenpwned),
    ("Image Metadata / EXIF", image_metadata),
    ("Tech Stack Detector", tech_stack_detector),
    ("Shodan Search", shodan_search),
    ("VirusTotal Check", virustotal_check),
]

