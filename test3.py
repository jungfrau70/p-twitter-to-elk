import twint

# Configure
c = twint.Config()
#c.Username = "realDonaldTrump"
c.Search = "tesla"

c.Store_csv = True
c.Output = "data"

twint.run.Search(c)
