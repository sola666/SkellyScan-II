
# def GetCNames(domain):
    #     try:
    #         answers = dns.resolver.query(domain, 'CNAME')
    #         for rdata in answers:
    #             print('CNAME', ':', rdata.to_text())

    #     except Exception as e:
    #         print(Fore.RED + 'Error: ' + str(e))  # or pass
            
    #GetCNames('http://support.nytimes.com')

# Section 1.2 - Arrays OUTDATED - REMOVE
    # Fingerprints is your fingerprints array.. Add to list as required.
    # Websites is your website array.. Add to list as required. All websites will be scanned for all fingerprints.
    # FingerPrints = ["<strong>Trying to access your account",
    #                        "Use a personal domain name",
    #                         "The request could not be satisfied",
    #                         "Sorry, We Couldn't Find That Page",
    #                         "Fastly error: unknown domain",
    #                         "The feed has not been found",
    #                         "You can claim it now at",
    #                         "Publishing platform",                        
    #                         "<title>No such app</title>",                        
    #                         "No settings were found for this company",
    #                         "<title>No such app</title>",
    #                         "is not a registered InCloud YouTrack.",
    #                         "You've Discovered A Missing Link. Our Apologies!",
    #                         "Sorry, couldn&rsquo;t find the status page",                        
    #                         "NoSuchBucket",
    #                         "Sorry, this shop is currently unavailable",
    #                         "<title>Hosted Status Pages for Your Company</title>",
    #                         "data-html-name=\"Header Logo Link\"",                        
    #                         "<title>Oops - We didn't find your site.</title>",
    #                         "class=\"MarketplaceHeader__tictailLogo\"",                        
    #                         "Whatever you were looking for doesn't currently exist at this address",
    #                         "The page you have requested does not exist",
    #                         "This UserVoice subdomain is currently available!",
    #                         "but is not configured for an account on our platform",
    #                         "Looks like you've traveled too far into cyberspace.",
    #                         "The specified bucket does not exist",
    #                         "Bad Request: ERROR: The request could not be satisfied",
    #                         "Please try again or try Desk.com free for",
    #                         "We could not find what you're looking for",
    #                         "No Site For Domain",
    #                         "Project doesnt exist... yet!",
    #                         "project not found",
    #                         "Please renew your subscription",
    #                         "Double check the URL or <a href=\"mailto:help@createsend.com",
    #                         "There is no portal here",
    #                         "You may have mistyped the address or the page may have moved",
    #                         "Repository not found",
    #                         "<title>404 &mdash; File not found</title>",
    #                         "This page is reserved for artistic dogs",
    #                         "<h1>The page you were looking for doesn",
    #                         "<h1>https://www.wishpond.com/404?campaign=true",
    #                         '<p class="bc-gallery-error-code">Error Code: 404</p>',
    #                         "<h1>Oops! We couldn&#8217;t find that page.</h1>",
    #                         "Unrecognized domain <strong>",
    #                         "NoSuchKey",
    #                         "The specified key does not exist",
    #                         "<title>Help Center Closed | Zendesk</title>"]
    # Websites = ['https://adv.nytimes.com/',
    #             'http://resources.news.com.au/',
    #             'http://support.nytimes.com']