from hapax3.py import legomena, dislegomena, trilegomena, vertical_export_to_filename

#input
filename = "Autobiography of Benjamin Franklin.txt"

#output
output_file = "hapax_legomena.txt"
vertical_export_to_filename(legomena(filename), output_file)

output_file2 = "hapax_dislegomena.txt"
vertical_export_to_filename(dislegomena(filename), output_file2)

output_file3 = "hapax_trilegomena.txt"
vertical_export_to_filename(trilegomena(filename),output_file3)


print("Results successfully exported as "+output_file+", "+output_file2+","+output_file3)
print("I had to export to a file, because Sublime Text refused to print certain characters...")
print("Calling an additional export function to make things even more modular")

