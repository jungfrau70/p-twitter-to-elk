import twint

# Configure
c = twint.Config()
#c.Username = "realDonaldTrump"
c.Search = "tesla"
c.Store_json = True
c.Elasticsearch = "localhost:9200"
#c.Skip_certs = True

twint.run.Profile(c)

