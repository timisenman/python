def string_clean(s):
	return s.translate(None, '0123456789')


print string_clean("")
print string_clean("! !")
print string_clean("123456789")
print string_clean("(E3at m2e2!!)")
print string_clean("Dsa32 cdsc34232 csa!!! 1I 4Am cool!")
print string_clean("A1 A1! AAA   3J4K5L@!!!")
print string_clean("Adgre2321 A1sad! A2A3A4 fv3fdv3J544K5L@")
print string_clean("Ad2dsad3ds21 A  1$$s122ad! A2A3Ae24 f44K5L@222222 ")
print string_clean("33333Ad2dsad3ds21 A3333  1$$s122a!d! A2!A!3Ae$24 f2##222 ")
print string_clean("My \"me3ssy\" d8ata issues2! Will1 th4ey ever, e3ver be3 so0lved?")
print string_clean("Wh7y can't we3 bu1y the goo0d software3? #cheapskates3")
