# Given map {X=>123, Y=456}
# Input: %X%_%Y%
# Output: 123_456
# Given map {USER=>admin, HOME=>/%USER%/home} Input: I am %USER% My home is %HOME% Output: I am admin My home is /admin/home
# USER= bob
# HOME= /home/%USER% should be substituted as : /home/bob ex2:
# home/ %USER% -> /home/bob
# Hello %USER% -> Hello bob!
# ex3:
# The user %USER% is at 50%% -> The user bob is at 50%