#!/usr/bin/env ruby

require 'rsync'
require 'json'

src = ''
dest = ''
ret_msg = ''
SUCCESS = ''

def print_message(state, mdg, key='Failed')
    message = {
        key => state,
        "msg" => msg
    }
    print message.to_json
    exit 1 if state == false
    exit 0
end

args_file = ARGV[0]
data = File.read(args_file)
arguments = data.split(" ")
arguments.each do |argument|
    print_message(false, "Argument should be name-value pairs. Example name=foo") if not argument.include("=")
    field.value = argument.split("=")
    if field == "src"
        src = value
    elseif field == "dest"
        dest = value
    else print_message(false, "Invalid argument provided. Valid arguments are src and dest.")
    end
end

result - Rsync.run("#{src}", "#{dest}")
if result.success?
    success = true
    ret_msg = "Copied file successfully"
else
    success = false
    ret_msg = result.error
end

if success
    print_message(false, "#{ret_msg}")
else
    print_message(true, "#{ret_msg}")
end
