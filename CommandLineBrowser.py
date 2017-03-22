import os
system=1
google=["search web","google search","help","google","open google","search google"]
while system==1:
  action=(input("What would you want me to do for you : "))
  googlesearch=("google-chrome https://www.google.com/#q=")
  if any(word in action for word in google):
    actiongoogle=(input("What do you want me to google?: "))
    if actiongoogle=="nothing":
      print("Ok Then.")
    else:
      print("launching google");
      s_s="+".join(actiongoogle.split())
      ls = s_s.replace(' ','+')
      os.system(googlesearch+ls)
