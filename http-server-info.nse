description = [[
Fetch HTTP server info: status, server header, and title
]]

author = "Madan Kumar"
license = "Same as Nmap"
categories = {"default", "safe"}

portrule = function(host, port)
    return port.number == 80 or port.number == 8080
end

action = function(host, port)
    local socket = nmap.new_socket()
    socket:connect(host.ip, port.number)

    socket:send("GET / HTTP/1.0\r\n\r\n")

    local response = socket:receive()
    socket:close()

    if response then
        local server = response:match("Server: ([^\r\n]+)")
        local status = response:match("HTTP/%d%.%d (%d+)")
        local title = response:match("<title>(.-)</title>")

        return string.format(
            "Status: %s\nServer: %s\nTitle: %s",
            status or "N/A",
            server or "N/A",
            title or "N/A"
        )
    end

    return "No response"
end
