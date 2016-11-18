import urllib


# Give the article doi, then generate necessary info to download the pdf file
# LibGen for scientific articles:
# http://libgen.io/scimag/ads.php?doi=
# Put in article title 

class GetArticlesFromLibGen():
	def __init__(self,doi,article_title):
		self.libgen_address = "http://libgen.io/scimag/ads.php?doi=" + doi 
		self.doi = doi 
		self.file_title = article_title	
		def CleanFileName(s):
			article_title = s.replace(" ", "_")
			final_article_title = ""
			for i in article_title:
				if i not in "?.!/;:":
					final_article_title = final_article_title + i
			return final_article_title

		self.file_name = CleanFileName(self.file_title) + ".pdf"


	def FetchTheArticleData(self):
		# About filename: MUST erase all special symbols to 
		# prevent IO error.

		# Fix the problem that some articles are not in LibGen


		address_primer = "http://libgen.io/scimag/get.php?doi="
		file_address_without_key = address_primer + self.doi + "&key="
		temp_html=urllib.urlopen(self.libgen_address)
		string_to_q = temp_html.read()
		book_file_url_start = string_to_q.find(file_address_without_key)
		book_file_url_end = string_to_q.find("'",book_file_url_start)
		libgen_file_address = string_to_q[book_file_url_start:book_file_url_end]
		return libgen_file_address


	def DownloadTheArticle(self):
	# If the ExceptionHandling return True 
	# Then download the file with file name:
	# self.file_name = article_title + ".pdf"
		downloader=urllib.FancyURLopener()
		downloader.retrieve(self.FetchTheArticleData(),self.file_name)