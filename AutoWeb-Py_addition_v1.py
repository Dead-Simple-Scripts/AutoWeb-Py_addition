import collections  # needed for Counter dictionary
import re
import sys
import datetime
import os

# Making argument to run script: python script.py <file path to log directory>
search_dir = sys.argv[1]
# Timestamp for file name
tstamp = datetime.datetime.now().strftime("%d-%m-%Y_%H%M%S")  # 03-11-2019_07:33:34  (24H)


# rex logic derived from pythex validation testing
# This will have to be adjusted slightly to align with weblog format
rex = r'^(?P<remote_host>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})(.+)(?P<date>\d{2}\/\w{3}\/\d{4})(.+)(?P<time>\d{2}\:\d{2}\:\d{2}).(?P<timezone>\W{1}\d{4})(\W{1,3})(\W)(?P<req_method>\w{3,10})(.)(?P<request>.+)(?P<protocol>HTTP[\d\W]{1,8})(")(.)(?P<resp_code>\d{3})(.)(?P<bytes>\d{1,12})(.{1,2})(?P<referrer>.+)(" ")(?P<user_agent>.+)(")'

# create counter dictionary
cnt_ips = collections.Counter()
cnt_req_method = collections.Counter()
cnt_resp_code = collections.Counter()
cnt_user_agent = collections.Counter()
cnt_bytes = collections.Counter()
cnt_referrer = collections.Counter()
cnt_request = collections.Counter()
cnt_date = collections.Counter()

# search 1: Remote Host Count
def remote_ip_analytics():
    ip_match = 0
    ip_fail = 0
    for root, dirs, files in os.walk(search_dir, onerror=None):  # walk the arg directory
        for filename in files:  # iterate over the files in the current dir
            file_path = os.path.join(search_dir, filename)  # build the file path
            try:
                with open(file_path, "rb") as f:  # open the file for reading
                    # read the file line by line
                    for line in f:  # use: "for i, line in enumerate(f)" if you need line numbers
                        try:
                            m = re.match(rex, line)  # match regex against each line
                            if m:
                                cnt_ips.update([m.group('remote_host')])
                                ip_match += 1
                            else:
                                ip_fail += 1
                        except ValueError:  # failed, skip the line
                            continue
            except (IOError, OSError):  # ignore read and permission errors
                pass
        # returning below values make them call-able into other definitions, needed for printing
        return ip_match, ip_fail


# search 2: HTTP Req Method
def http_req_method_analytics():
    req_method_match = 0
    req_method_fail = 0
    for root, dirs, files in os.walk(search_dir, onerror=None):  # walk the arg directory
        for filename in files:  # iterate over the files in the current dir
            file_path = os.path.join(search_dir, filename)  # build the file path
            try:
                with open(file_path, "rb") as f:  # open the file for reading
                    # read the file line by line
                    for line in f:  # use: for i, line in enumerate(f) if you need line numbers
                        try:
                            m = re.match(rex, line)  # match regex against each line
                            if m:
                                cnt_req_method.update([m.group('req_method')])
                                req_method_match += 1
                            else:
                                req_method_fail += 1
                        except ValueError:  # failed, skip the line
                            continue
            except (IOError, OSError):  # ignore read and permission errors
                pass
        # returning below values make them call-able into other definitions, needed for printing
        return req_method_match, req_method_fail


# search 3: HTTP Response codes
def http_resp_code_analytics():
    resp_code_match = 0
    resp_code_fail = 0
    for root, dirs, files in os.walk(search_dir, onerror=None):  # walk the arg directory
        for filename in files:  # iterate over the files in the current dir
            file_path = os.path.join(search_dir, filename)  # build the file path
            try:
                with open(file_path, "rb") as f:  # open the file for reading
                    # read the file line by line
                    for line in f:  # use: for i, line in enumerate(f) if you need line numbers
                        try:
                            m = re.match(rex, line)  # match regex against each line
                            if m:
                                cnt_resp_code.update([m.group('resp_code')])
                                resp_code_match += 1
                            else:
                                resp_code_fail += 1
                        except ValueError:  # failed, skip the line
                            continue
            except (IOError, OSError):  # ignore read and permission errors
                pass
        # returning below values make them call-able into other definitions, needed for printing
        return resp_code_match, resp_code_fail

# search 4: User Agents
def user_agent_analytics():
    user_agent_match = 0
    user_agent_fail = 0
    for root, dirs, files in os.walk(search_dir, onerror=None):  # walk the arg directory
        for filename in files:  # iterate over the files in the current dir
            file_path = os.path.join(search_dir, filename)  # build the file path
            try:
                with open(file_path, "rb") as f:  # open the file for reading
                    # read the file line by line
                    for line in f:  # use: for i, line in enumerate(f) if you need line numbers
                        try:
                            m = re.match(rex, line)  # match regex against each line
                            if m:
                                cnt_user_agent.update([m.group('user_agent')])
                                user_agent_match += 1
                            else:
                                user_agent_fail += 1
                        except ValueError:  # failed, skip the line
                            continue
            except (IOError, OSError):  # ignore read and permission errors
                pass
        # returning below values make them call-able into other definitions, needed for printing
        return user_agent_match, user_agent_fail

# search 5: Byte Count
def bytes_analytics():
    bytes_match = 0
    bytes_fail = 0
    for root, dirs, files in os.walk(search_dir, onerror=None):  # walk the arg directory
        for filename in files:  # iterate over the files in the current dir
            file_path = os.path.join(search_dir, filename)  # build the file path
            try:
                with open(file_path, "rb") as f:  # open the file for reading
                    # read the file line by line
                    for line in f:  # use: for i, line in enumerate(f) if you need line numbers
                        try:
                            m = re.match(rex, line)  # match regex against each line
                            if m:
                                cnt_bytes.update([m.group('bytes')])
                                bytes_match += 1
                            else:
                                bytes_fail += 1
                        except ValueError:  # failed, skip the line
                            continue
            except (IOError, OSError):  # ignore read and permission errors
                pass
        # returning below values make them call-able into other definitions, needed for printing
        return bytes_match, bytes_fail

# search 6: Referrer
def referrer_analytics():
    referrer_match = 0
    referrer_fail = 0
    for root, dirs, files in os.walk(search_dir, onerror=None):  # walk the arg directory
        for filename in files:  # iterate over the files in the current dir
            file_path = os.path.join(search_dir, filename)  # build the file path
            try:
                with open(file_path, "rb") as f:  # open the file for reading
                    # read the file line by line
                    for line in f:  # use: for i, line in enumerate(f) if you need line numbers
                        try:
                            m = re.match(rex, line)  # match regex against each line
                            if m:
                                cnt_referrer.update([m.group('referrer')])
                                referrer_match += 1
                            else:
                                referrer_fail += 1
                        except ValueError:  # failed, skip the line
                            continue
            except (IOError, OSError):  # ignore read and permission errors
                pass
        # returning below values make them call-able into other definitions, needed for printing
        return referrer_match, referrer_fail


# search 7: Request
def request_analytics():
    request_match = 0
    request_fail = 0
    for root, dirs, files in os.walk(search_dir, onerror=None):  # walk the arg directory
        for filename in files:  # iterate over the files in the current dir
            file_path = os.path.join(search_dir, filename)  # build the file path
            try:
                with open(file_path, "rb") as f:  # open the file for reading
                    # read the file line by line
                    for line in f:  # use: for i, line in enumerate(f) if you need line numbers
                        try:
                            m = re.match(rex, line)  # match regex against each line
                            if m:
                                cnt_request.update([m.group('request')])
                                request_match += 1
                            else:
                                request_fail += 1
                        except ValueError:  # failed, skip the line
                            continue
            except (IOError, OSError):  # ignore read and permission errors
                pass
        # returning below values make them call-able into other definitions, needed for printing
        return request_match, request_fail


# search 8: Date
def date_analytics():
    date_match = 0
    date_fail = 0
    for root, dirs, files in os.walk(search_dir, onerror=None):  # walk the arg directory
        for filename in files:  # iterate over the files in the current dir
            file_path = os.path.join(search_dir, filename)  # build the file path
            try:
                with open(file_path, "rb") as f:  # open the file for reading
                    # read the file line by line
                    for line in f:  # use: for i, line in enumerate(f) if you need line numbers
                        try:
                            m = re.match(rex, line)  # match regex against each line
                            if m:
                                cnt_date.update([m.group('date')])
                                date_match += 1
                            else:
                                date_fail += 1
                        except ValueError:  # failed, skip the line
                            continue
            except (IOError, OSError):  # ignore read and permission errors
                pass
        # returning below values make them call-able into other definitions, needed for printing
        return date_match, date_fail


# Output for search 1: Output Remote Hosts
def remote_ip_analytics_results():
    # Top 10 most frequent
    try:
        output_file_1 = ('remote_ip_analytics_' + tstamp + '_.txt')
        # calling ip_match and ip_fail results from search defimition
        match, fail = remote_ip_analytics()
        stdout_backup = sys.stdout # needed for printing system output
        with open(output_file_1, 'a') as f:
            sys.stdout = f
            print('[*] Search 1 Results: Remote IP Analytics')
            print('[*] ============================================')
            print('[*] %d lines matched the regular expression' % (match))
            print('[*] %d lines failed to match the regular expression' % (fail))
            print('[*] ============================================')
            print('[*] 10 Most Frequently Occurring Remote IPs')
            print('[*] ============================================')
            for remote_host, count in cnt_ips.most_common(10):
                print('[*] %30s: %d' % (remote_host, count))
            print('[*] ============================================')
            # Top 10 most rare
            print('[*] ============================================')
            print('[*] 10 Most Rarely Occurring Remote IPs')
            print('[*] ============================================')
            for remote_host, count in cnt_ips.most_common()[:-11:-1]:
                print('[*] %30s: %d' % (remote_host, count))
            print('[*] ============================================')
        sys.stdout = stdout_backup
        sys.stdout.close()
    except:
        pass

# Output for search 2: http req method
def http_req_method_analytics_results():
    # All results
    try:
        # calling match and fail results from search defimition
        output_file_2 = ('http_req_method_analytics_' + tstamp + '_.txt')
        match, fail = http_req_method_analytics()
        stdout_backup = sys.stdout
        with open(output_file_2, 'a') as f:
            sys.stdout = f
            print('[*] Search 2 Results: HTTP Request Method Analytics')
            print('[*] ============================================')
            print('[*] %d lines matched the regular expression' % (match))
            print('[*] %d lines failed to match the regular expression' % (fail))
            print('[*] ============================================')
            print('[*] All HTTP Request Methods')
            print('[*] ============================================')
            for req_method, count in cnt_req_method.most_common(25):
                print('[*] %30s: %d' % (req_method, count))
            print('[*] ============================================')
        sys.stdout = stdout_backup
        sys.stdout.close()
    except:
        pass


# Output for search 3: http response codes
def http_resp_code_analytics_results():
    # All results
    try:
        # calling match and fail results from search defimition
        output_file_3 = ('http_resp_code_analytics_' + tstamp + '_.txt')
        match, fail = http_resp_code_analytics()
        stdout_backup = sys.stdout
        with open(output_file_3, 'a') as f:
            sys.stdout = f
            print('[*] Search 3 Results: HTTP Response Code Analytics')
            print('[*] ============================================')
            print('[*] %d lines matched the regular expression' % (match))
            print('[*] %d lines failed to match the regular expression' % (fail))
            print('[*] ============================================')
            print('[*] All HTTP Response Codes')
            print('[*] ============================================')
            for resp_code, count in cnt_resp_code.most_common(100):
                print('[*] %30s: %d' % (resp_code, count))
            print('[*] ============================================')
        sys.stdout = stdout_backup
        sys.stdout.close()
    except:
        pass


# Output for search 4: User Agents
def user_agent_analytics_results():
    # All results
    try:
        # calling match and fail results from search defimition
        output_file_4 = ('user_agent_analytics_' + tstamp + '_.txt')
        match, fail = user_agent_analytics()
        stdout_backup = sys.stdout
        with open(output_file_4, 'a') as f:
            sys.stdout = f
            print('[*] Search 4 Results: User Agents Analytics')
            print('[*] ============================================')
            print('[*] %d lines matched the regular expression' % (match))
            print('[*] %d lines failed to match the regular expression' % (fail))
            print('[*] ============================================')
            print('[*] All User Agents')
            print('[*] ============================================')
            for user_agent, count in cnt_user_agent.most_common(100):
                print('[*] %30s: %d' % (user_agent, count))
            print('[*] ============================================')
        sys.stdout = stdout_backup
        sys.stdout.close()
    except:
        pass

# Output for search 5: Bytes Count
def bytes_analytics_results():
    # All results
    try:
        # calling match and fail results from search defimition
        output_file_5 = ('bytes_analytics_' + tstamp + '_.txt')
        match, fail = bytes_analytics()
        stdout_backup = sys.stdout
        with open(output_file_5, 'a') as f:
            sys.stdout = f
            print('[*] Search 5 Results: Byte Count Analytics')
            print('[*] ============================================')
            print('[*] %d lines matched the regular expression' % (match))
            print('[*] %d lines failed to match the regular expression' % (fail))
            print('[*] ============================================')
            print('[*] All Byte Counts')
            print('[*] ============================================')
            for bytes, count in cnt_bytes.most_common(100):
                print('[*] %30s: %d' % (bytes, count))
            print('[*] ============================================')
        sys.stdout = stdout_backup
        sys.stdout.close()
    except:
        pass

# Output for search 6: Referrer
def referrer_analytics_results():
    # All results
    try:
        # calling match and fail results from search defimition
        output_file_6 = ('referrer_analytics_' + tstamp + '_.txt')
        match, fail = referrer_analytics()
        stdout_backup = sys.stdout
        with open(output_file_6, 'a') as f:
            sys.stdout = f
            print('[*] Search 6 Results: Referrer Analytics')
            print('[*] ============================================')
            print('[*] %d lines matched the regular expression' % (match))
            print('[*] %d lines failed to match the regular expression' % (fail))
            print('[*] ============================================')
            print('[*] All Referrers')
            print('[*] ============================================')
            for referrer, count in cnt_referrer.most_common(100):
                print('[*] %30s: %d' % (referrer, count))
            print('[*] ============================================')
        sys.stdout = stdout_backup
        sys.stdout.close()
    except:
        pass

# Output for search 7: Request
def request_analytics_results():
    # All results
    try:
        # calling match and fail results from search defimition
        output_file_7 = ('request_analytics_' + tstamp + '_.txt')
        match, fail = request_analytics()
        stdout_backup = sys.stdout
        with open(output_file_7, 'a') as f:
            sys.stdout = f
            print('[*] Search 7 Results: Request Analytics')
            print('[*] ============================================')
            print('[*] %d lines matched the regular expression' % (match))
            print('[*] %d lines failed to match the regular expression' % (fail))
            print('[*] ============================================')
            print('[*] All Resource Requests')
            print('[*] ============================================')
            for request, count in cnt_request.most_common(100):
                print('[*] %30s: %d' % (request, count))
            print('[*] ============================================')
        sys.stdout = stdout_backup
        sys.stdout.close()
    except:
        pass

# Output for search 8: Date
def date_analytics_results():
    # All results
    try:
        # calling match and fail results from search defimition
        output_file_8 = ('date_analytics_' + tstamp + '_.txt')
        match, fail = date_analytics()
        stdout_backup = sys.stdout
        with open(output_file_8, 'a') as f:
            sys.stdout = f
            print('[*] Search 8 Results: Date Analytics')
            print('[*] ============================================')
            print('[*] %d lines matched the regular expression' % (match))
            print('[*] %d lines failed to match the regular expression' % (fail))
            print('[*] ============================================')
            print('[*] All Dates')
            print('[*] ============================================')
            for date, count in cnt_date.most_common(100):
                print('[*] %30s: %d' % (date, count))
            print('[*] ============================================')
        sys.stdout = stdout_backup
        sys.stdout.close()
    except:
        pass

# MAIN CODE
if __name__ == '__main__':
    remote_ip_analytics()
    remote_ip_analytics_results()

    http_req_method_analytics()
    http_req_method_analytics_results()

    http_resp_code_analytics()
    http_resp_code_analytics_results()

    user_agent_analytics()
    user_agent_analytics_results()

    bytes_analytics()
    bytes_analytics_results()

    referrer_analytics()
    referrer_analytics_results()

    request_analytics()
    request_analytics_results()

    date_analytics()
    date_analytics_results()
