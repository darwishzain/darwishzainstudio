import argparse,os,shutil,zipfile

parser = argparse.ArgumentParser(description='Extract and delete ZIP')
parser.add_argument('-d','--zipfile',type=str,required=True,help='Path to ZIP file')

args = parser.parse_args()

file = args.zipfile

if not os.path.exists(file):
	print(f"Error: File {file} don't exist")
else:
	extractto = os.path.splitext(os.path.basename(file))[0].lower()

	with zipfile.ZipFile(file,'r') as ref:
		ref.extractall(extractto)
		print(f"Extracted to {extractto}/")
	os.remove(file)
	print(f"Remove ZIP file: {file}")

