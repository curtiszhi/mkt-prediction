import os, multiprocessing as mp

# process file function

filename = 'Users/curtiszhi/Desktop/Archives/BoA/MARK/stock_data/AAPL.csv'


def processfile(filename, start=0, stop=0):
    if start == 0 and stop == 0:
#         ... process entire file...
        pass
    else:
        with open(filename, 'r') as fh:
            fh.seek(start)
            lines = fh.readlines(stop - start)
#             ... process these lines ...

    return results

if __name__ == "__main__":

    # get file size and set chuck size
    filesize = os.path.getsize(filename)
    split_size = 100*1024*1024

    # determine if it needs to be split
    if filesize > split_size:

        # create pool, initialize chunk start location (cursor)
        pool = mp.Pool(mp.cpu_count)
        cursor = 0
        results = []
        with open(filename, 'r') as fh:

            # for every chunk in the file...
            for chunk in range(filesize // split_size):

                # determine where the chunk ends, is it the last one?
                if cursor + split_size > filesize:
                    end = filesize
                else:
                    end = cursor + split_size

                # seek to end of chunk and read next line to ensure you 
                # pass entire lines to the processfile function
                fh.seek(end)
                fh.readline()

                # get current file location
                end = fh.tell()

                # add chunk to process pool, save reference to get results
                proc = pool.apply_async(processfile, args=[filename, cursor, end])
                results.append(proc)

                # setup next chunk
                cursor = end

        # close and wait for pool to finish
        pool.close()
        pool.join()

        # iterate through results
        for proc in results:
            processfile_result = proc.get()

    else:
#         ...process normally...