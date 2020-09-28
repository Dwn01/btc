impor  kembali
waktu impor
impor  os
impor  sys
impor  acak

penebangan . basicConfig ( level = logging . ERROR )

dari  telethon  impor  TelegramClient , peristiwa
dari  telethon . tl . fungsi . saluran  mengimpor  JoinChannelRequest
dari  telethon . tl . fungsi . impor pesan  GetBotCallbackAnswerRequest 
dari  datetime  import  datetime
dari  colorama  import  Fore , init  sebagai  color_ama
color_ama ( autoreset = True )



coba :
   impor  colorama
   dari  colorama  import  Fore , Back , Style
   colorama . init ( autoreset = True )
   hijau  =  Gaya . RESET_ALL + Gaya . BRIGHT + Fore . HIJAU
   res  =  Gaya . RESET_ALL
   abu2  =  Gaya . DIM + Fore . PUTIH
   putih  =  Gaya . RESET_ALL + Gaya . BRIGHT + Fore . PUTIH
   ungu2  =  Gaya . NORMAL + Kedepan . MAGENTA
   ungu  =  Gaya . RESET_ALL + Gaya . BRIGHT + Fore . MAGENTA
   hijau2  =  Gaya . NORMAL + Kedepan . HIJAU
   yellow2  =  Gaya . NORMAL + Kedepan . KUNING
   kuning  =  Gaya . RESET_ALL + Gaya . BRIGHT + Fore . KUNING
   red2  =  Gaya . NORMAL + Kedepan . MERAH
   merah  =  Gaya . RESET_ALL + Gaya . BRIGHT + Fore . MERAH
   cyan  =  Gaya . RESET_ALL + Gaya . BRIGHT + Fore . CYAN
   cyan2  =  Gaya . NORMAL + Kedepan . CYAN

kecuali :
   print ( "Harap Instal Modul Colorama !! \ n \ n \ n " )
   sys . keluar ()

coba :
    permintaan impor
   dari  bs4  import  BeautifulSoup
kecuali :
   print ( "Harap Instal Permintaan Modul & BS4 \ n \ n \ n " )
   sys . keluar ()

os . sistem ( 'cls'  if  os . name == 'nt'  else  'clear' )

# Dapatkan nilai Anda sendiri dari my.telegram.org
api_id  =  1992530
api_hash  =  '5c8aeda6f752d74363769d456913665c'

spanduk  =  "" "
"" " + Gaya . CERAH + Kedepan . CYAN + " ""
\ 033 [1; 32m╔═══════════════════════════════════════════ ═════╗
\ 033 [1; 32m║Didukung: SHPC7BOT ║
\ 033 [1; 32m║Terima Kasih Khusus: SEMUA TIM SAYA ║
\ 033 [1; 32m║Saluran video: SHPChannels ║
\ 033 [1; 32m║Telegram grup: SHPCorps7 ║
\ 033 [1; 32m║Doge Donate: Gratis ║
\ 033 [1; 32m╚═══════════════════════════════════════════ ═════╝
"" " + Style . RESET_ALL + Style . BRIGHT + Fore . WHITE + " "" [Dibuat oleh SHPC7 2020] "" "

cname  =  '@BTC_Ads_de_bot'
crot  =  'https://t.me/BTC_Ads_de_bot'

def  print_msg_time ( pesan ):
	print ( '['  +  Fore . CYAN  +  f ' { datetime . now (). strftime ( "% H:% M:% S" ) } '  +  Fore . RESET  +  f '] { message } ' )

async  def  main ():
	cetak ( spanduk )
	cetak ( Fore . BLUE  +  '=========================================== ====== \ n '  +  Fore . RESET )
	
	# Periksa apakah nomor telepon tidak ditentukan

	jika  len ( sys . argv ) <  2 :
		print ( 'Penggunaan: python start.py phone_number' )
		print ( '-> Masukkan nomor dalam format internasional (contoh: + 62xxxxxxxxxx) \ n ' )
		e  =  input ( 'Tekan sembarang tombol untuk keluar ...' )
		keluar ( 1 )
		
	phone_number  =  sys . argv [ 1 ]
	choice  =  '🎯Lihat Iklan'
	
	jika  tidak  os . jalan . ada ( "sesi" ):
		os . mkdir ( "sesi" )
   
    # Hubungkan ke klien
	klien  =  TelegramClient ( 'session /'  +  phone_number , api_id , api_hash )
	menunggu  klien . mulai ( phone_number )
	me  =  menunggu  klien . get_me ()
	
	# Free_LTC_Robot
	print_msg_time ( Fore . GREEN  +  f'Name: @BTC_Ads_de_bot '   +  Fore . RESET )
	print_msg_time ( Fore . GREEN  +  f'Welcome: { saya . first_name } - { saya . last_name } '   +  Fore . RESET )
	cetak ( f ' \ n ' )
	print_msg_time ( Fore . KUNING  +  'Mulai Bot'  +  ' \ n '  +  Fore . RESET )
	
	# Mulai perintah / keseimbangan

	i  =  1
	sementara ( Benar ):
		menunggu  klien . send_message ( crot , pilihan )
		print_msg_time ( Fore . GREEN  +  'Klik Sukses >>'  +  pilihan  +  Fore . RESET )
		waktu . sleep ( 37 ) #waktu klik hitungan dalam detik
		i  =  1
		
	
		# Kirim pesan ke bot
	@ klien . on ( peristiwa . NewMessage ( chats = cname , incoming = True ))
	async  def  generated_amount ( event ):
		pesan  =  acara . raw_text
		jika  'Balance'  di  pesan :	
			print_msg_time ( Fore . GREEN  +  acara . raw_text  +  ' \ n '  +  Fore . RESET )
		
			
	menunggu  klien . run_until_disconnected ()
	
asyncio . get_event_loop (). run_until_complete ( main ())
