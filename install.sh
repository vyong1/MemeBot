echo "This script is incomplete (gonna finish it later)"
#? Clean
# rm -rf files/CachedRequests
# mkdir files/CachedRequests

# if [ -f files/memepic.png ]; then
#     rm files/memepic.png
# fi

# if [ -f files/MemeDict.json ]; then
#     rm files/MemeDict.json
# fi

# if [ -f files/prev_req_time.txt ]; then
#     rm files/prev_req_time.txt
# fi

# # Install
# cd files
# touch prev_req_time.txt
# # Initialize the previous request time to guarantee that
# # there's a GET request on startup
# printf "2000-01-01 00:00:00.000000" > prev_req_time.txt 

# if [ ! -f token.txt ]; then
#     touch token.txt
#     echo "Ask vyong for the token"
#     echo "then copy and paste it into token.txt"
#     echo ""
#     echo "Make sure you NEVER give out the token!"
#     echo "It lets intruders into the server"
# fi

# cd ..