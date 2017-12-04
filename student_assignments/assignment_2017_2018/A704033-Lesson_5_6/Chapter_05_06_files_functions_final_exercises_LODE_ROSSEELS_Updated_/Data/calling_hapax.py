from hapax3.py import legomena, dislegomena, trilegomena, vertical_export_to_filename

#input
filename = "Autobiography of Benjamin Franklin.txt"

#output
outputname = " - hapax legomena"
vertical_export_to_filename(filename,legomena(filename),outputname)

outputname = " - hapax dislegomena"
vertical_export_to_filename(filename,dislegomena(filename),outputname)

outputname = " - hapax trilegomena"
vertical_export_to_filename(filename,trilegomena(filename),outputname)

print("I had to export to a file, because Sublime Text refused to print certain characters...")
print("Calling an additional export function to make things even more modular")
