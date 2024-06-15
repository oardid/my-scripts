local http = require "http"
local shortport = require "shortport"

description = [[ Fetches and displays HTTP headers from the target web server. ]]

author = "Omar"

portrule = shortport.http

action = function(host, port)
  local response = http.get(host, port, "/")
  if response then
    return response.header
  else
    return "Failed to retrieve HTTP headers."
  end
end
