import re
import numpy as np

from aoc_lib import solve_problem

INPUT = '''hgg{m>732:R,A}
vzp{s>1750:A,A}
kvs{x<1064:dnd,R}
hq{s<952:jpz,m<3318:qkp,a<2869:vzp,zgn}
zdf{a<2840:kxm,m<1054:dxj,a<3470:cq,pch}
sd{x>2576:R,x<1498:R,pkt}
zgb{s>2352:A,m<2764:jt,hcb}
hfj{a<701:R,m>3080:A,x<2249:A,A}
pn{x>1276:R,m>1276:R,A}
nd{x<3651:R,x>3846:R,a>3644:A,A}
sbc{x>2524:tq,x>1070:hl,s>3271:hxp,nh}
jt{s<1280:R,a>1851:R,s>1766:A,R}
rxr{s<3803:A,R}
rr{x>447:pxs,mz}
kdf{x>2925:hbk,x>2219:nx,zrm}
jfc{s>3141:R,m>3845:A,a<806:R,bqd}
lx{s<1052:A,s<1932:R,gkq}
jb{a>3318:A,s>111:R,R}
kfl{m<2645:R,A}
fg{a<3713:R,a>3835:A,A}
jbv{s>1566:zlj,m<3564:hh,x>366:nsd,A}
zth{m>2830:A,lgd}
zlj{m<3411:A,a>2553:A,m<3762:A,R}
ctc{s<1469:zp,a<2046:vfm,rqx}
zn{x>291:hc,x>101:R,A}
lcx{x<3566:A,a>2592:A,A}
zk{a<3309:R,R}
tl{x>895:A,a<732:R,R}
kdb{x>845:R,zk}
qgk{s<2732:R,x>2908:A,s>3010:R,zr}
hsm{s<3360:A,A}
sfp{m>3895:R,s<1358:A,m>3804:R,R}
cl{x>2049:R,x<870:zxm,R}
tx{x>2307:R,s<3681:R,m>3382:A,R}
stv{x<2190:R,A}
cfz{a<3857:R,R}
gtb{s<3465:R,s<3670:A,x>1757:A,A}
zs{m>984:pjk,sh}
tcj{a<1184:R,A}
pm{s<3393:A,s<3755:R,A}
gdz{m<3542:A,m>3594:A,a<1498:A,R}
nzb{x<3011:R,jgz}
sn{s<3550:R,R}
tpk{s<3778:bc,R}
hkm{x>1129:R,m>3753:R,A}
zj{x>429:hfm,s<1850:qtd,m>2398:pl,ck}
hpc{m<2206:pm,a>3713:A,A}
nzg{s<3043:zb,m>2858:jn,m>2708:mq,A}
kmj{s<2167:A,R}
xd{x>870:A,bnf}
qvb{a<3340:drt,s<3669:bxl,m<2555:A,A}
gm{x<936:jzq,a>3483:hqn,jc}
xn{a>2420:A,m<3358:R,s<3579:A,R}
mr{a<2812:R,x<1699:jb,A}
vt{x>1719:R,s<3007:A,A}
qfl{s<2232:R,R}
rdc{m<2182:A,x<1575:A,A}
gl{m>1093:A,A}
fs{x>1079:nzn,s>1157:kgv,x>571:xd,xth}
nfr{s<2860:A,x<1572:R,m>3768:R,A}
mfj{m<2770:sk,x>1181:frs,R}
vd{m<1234:xp,s>2257:svj,vtc}
hsb{s>482:A,s>284:R,A}
fd{a<252:xml,m<3318:nmv,fpl}
mmm{s>2345:A,x<1713:R,s>1117:R,A}
hbk{a<3025:A,x>3291:kvm,A}
dnd{a<2368:R,m<2230:R,m<2369:A,A}
in{m<1990:qjf,a>2159:xgh,dpb}
tv{m>1654:R,a>3358:A,m<1380:A,A}
th{s>2207:R,m>1565:R,s>2011:fl,A}
hv{a<716:R,qp}
vqs{a>2347:R,s<2796:R,R}
fv{s<2752:tr,lf}
cpr{m>3491:A,s>3797:A,A}
ds{m<3334:R,R}
rg{s<2348:sz,m>718:nzt,gh}
vzs{s<1742:fd,dp}
xtm{a<2584:xgj,x>1663:ltj,s>3178:sxl,pk}
hm{m>2461:xx,vm}
ksz{a>1434:A,m>3082:A,A}
scb{x<2008:R,m<558:dvd,R}
vp{x<1485:A,R}
mjx{s>651:A,R}
kzj{s>1541:A,a<695:A,s<886:A,R}
dbj{m>3361:lqd,ltk}
gts{s>2787:A,m<3808:R,a>2824:A,R}
kg{x>3620:A,R}
vf{a>1337:A,R}
jgz{s>2888:A,a>3453:R,a<3176:A,R}
rmt{s<2230:km,m<2483:bqc,m<2627:pgm,cb}
hqn{s>3478:ff,msp}
mjg{s<2639:mqt,a<2805:kzv,a>2899:ltz,A}
qjn{x>3835:R,s>2114:A,R}
rx{a>1351:hgg,m>1301:vf,x<1400:R,A}
mh{m<3081:R,A}
txx{x>3662:A,x>3543:A,R}
njk{a>2981:nzb,m>3249:kbz,x>3107:llq,xm}
bg{m>2769:lrm,x>1412:nqv,x>780:rmt,zj}
vnt{m>3183:A,s<1605:R,R}
fc{s<2876:A,s<2956:A,a<2617:R,A}
pbq{s<1098:pfs,A}
kk{x>3057:R,a>1356:R,x<2360:R,A}
hc{x<490:R,a>2332:R,s<2713:R,R}
fzl{s>2412:R,qg}
ppq{m<2160:xtd,R}
gp{m<844:A,x<721:A,m>1253:A,R}
bxl{s>3312:R,R}
tt{x>1574:A,bh}
gz{a>2385:A,x>2724:R,A}
zrm{s<2838:A,a>2798:mnt,m>3576:ftm,lnx}
ttb{s<1415:ntt,a<3785:R,tsq}
dtr{a>2609:vcv,R}
mj{a<1260:zps,mv}
hcb{x>1573:R,m>3278:A,R}
dnc{x<2421:kcs,x>3012:krl,sxx}
tq{x<3454:nfg,bz}
spr{a>3610:jvx,a<3585:fll,m<2508:R,fx}
hz{s<2826:A,x<3418:R,x>3473:A,A}
qt{s<3401:R,a>2827:A,s<3488:A,R}
nx{s>2882:fb,a>3202:qrr,x<2643:R,ml}
zgn{m>3646:nr,s<1935:R,gc}
hxs{x>2889:R,A}
nsd{s<1022:R,x<711:R,R}
mz{m>3396:R,R}
zxb{s>2200:lxk,s<1081:jg,a<967:R,A}
mq{s<3660:R,s<3830:R,R}
mm{a<2121:kl,dq}
ljl{a>2625:A,s<715:R,x<987:R,A}
gd{x>325:A,m>3623:A,m>3593:R,A}
mjb{m>1315:th,a<1048:qfl,pf}
xth{x>253:gf,m<3418:R,a>3249:R,A}
qrr{x<2567:R,x<2740:A,A}
vn{s<1422:R,m>3090:R,x>1358:A,A}
vs{x<3425:lm,x<3711:zpp,a>3240:A,R}
sx{x>1154:hgr,s<3286:R,m>2956:mbk,vv}
zjx{s>2859:xq,a>2727:mjg,x>348:brq,dg}
dmh{s<1545:A,s<2869:R,A}
tcv{m>2415:R,s<2869:A,a>1121:A,A}
kx{m>2513:sq,R}
nj{s>2137:R,m<2396:A,A}
zhx{s<2307:A,m>3073:A,x<1427:A,A}
qkx{a>571:pqx,fzl}
tr{x<2538:rg,a>1704:vd,mjb}
jc{s<3408:zd,m>3255:jp,s<3755:R,mn}
drt{a>3088:A,R}
vtc{s>2003:A,x<3154:hxs,a>3124:cr,A}
jjc{x>3540:A,s<2573:R,R}
zgx{m>3587:hkm,s>3105:scv,fc}
bjk{x>3546:R,a>2820:R,A}
hpz{a>501:R,m<2895:R,m>2940:A,A}
jx{m<3451:pbq,x>2949:kg,x>2571:nt,lx}
qkp{m<3004:A,a>2889:R,x<1884:A,vnt}
pkb{x<1686:vjg,mj}
vnp{s<1061:mpc,m>3578:tl,jtz}
ffs{s<2916:R,a<2299:R,R}
mv{x>3123:R,x>2553:R,s>2651:fhn,cbj}
prn{s>697:zs,rt}
mb{s<1405:A,R}
ss{x<2935:A,R}
vx{s>2731:R,R}
bk{s<2882:hfl,m<2777:R,x<864:A,ngk}
hfm{m<2257:lcv,s>2171:rv,A}
jh{x<2941:A,x<3595:A,x>3818:R,A}
jds{m<3855:gts,R}
ks{a<3503:kdb,x>1187:ppq,hpc}
bd{a>466:A,a<245:R,m>1689:A,A}
mfc{x>3526:pd,x>3237:hz,s<2700:R,A}
pqg{a>3770:A,x<3148:A,s>3674:R,A}
ppv{a>1791:zgb,zth}
kd{m>2478:R,a>3578:A,m>2204:R,A}
dr{m>2619:sx,a>2224:nz,m>2301:tzf,lcn}
vvv{s<2624:R,A}
tnh{s>455:crj,sd}
xz{m<2785:R,a<108:A,A}
fz{m>333:A,R}
jn{a>2407:R,A}
lrm{a<661:dcc,a>776:zh,btk}
hmr{m<2368:A,A}
nmz{x>693:R,m>3188:A,m>3058:R,R}
frs{m>3249:A,a<221:R,R}
jtr{m>2442:R,a<3661:A,A}
jnb{a<3040:A,x>3255:A,m>2681:R,gqp}
czx{a<2797:qgk,x>2667:vs,cj}
dxj{x<1473:A,m>646:A,gn}
dkc{a<3192:A,x>2652:A,R}
brn{m>2483:R,R}
hgq{x>2571:dh,a>3047:pn,rqd}
vm{m<2295:R,x<1501:vfz,R}
zrx{x>3664:R,R}
xp{s<2156:A,x<3245:A,m>713:A,R}
frc{x>1723:A,s<765:rnd,s>1228:R,R}
vzn{m<3662:xn,m>3789:pmq,x<346:sps,knz}
tzp{a<2601:A,R}
sbv{s<3256:A,m>3843:A,R}
pgm{x<1039:thc,a<697:xl,s>3363:xk,vx}
txh{m>817:vb,x>2055:R,a>3331:fg,A}
hl{s<3381:A,a>949:pbx,A}
pv{x<3278:mcn,A}
bp{a<3740:hsm,R}
nfv{a>2817:sn,s>3526:A,R}
krl{x>3664:ln,R}
gn{m>318:R,s<1312:R,A}
vgh{m<3240:R,m<3680:A,m>3809:A,A}
lxk{s>3196:A,a>964:A,R}
jlq{m>3890:bbh,a>749:R,s>2957:kf,A}
ltk{a<746:kzj,s<2010:lbb,s>2702:R,bn}
bnf{m<3676:R,a<3211:A,R}
btk{m<2914:R,hfj}
kf{s<3575:A,a>731:R,a<717:R,R}
mf{s<918:qc,bd}
vq{x<2684:tx,s>3597:dc,m>3578:R,txp}
px{x<1800:A,A}
vng{s>2468:dfj,rpp}
msl{a>2341:qnv,m<3402:dk,s>2812:ffs,A}
xtd{m<2065:A,m<2123:A,A}
vb{s>565:R,R}
nzn{m<3567:rl,A}
pvf{m<3022:czx,m<3434:njk,m<3770:kdf,zq}
mnt{a>3211:R,a>3068:R,a<2951:R,R}
zq{s<2963:jds,qcs}
fgq{m<3512:nmz,a>1362:hsh,A}
zb{x<1166:A,A}
pkt{a>3352:A,s>297:R,A}
cdv{m>2207:A,a>757:R,R}
zzl{s>1119:A,m<1401:A,A}
vkc{m<3684:A,a<564:A,A}
ppl{s>1486:A,a<2541:R,s<1386:A,R}
dps{x>3282:fj,dgg}
pxn{x>646:A,A}
jhk{x>481:R,m>1575:R,R}
vl{a<2877:A,R}
dg{a>2578:A,s<2674:kz,x>158:zdp,gcx}
nmv{a<337:A,kst}
tn{a<2905:jgv,kbm}
gs{a<604:R,a>686:R,A}
rc{m<3404:A,R}
kz{m>3485:R,A}
cs{a>1936:ctc,x<2481:ppv,s<1840:tsd,jlz}
dvd{s>930:R,A}
qtd{x>235:R,s>1101:A,m<2340:R,brn}
nk{s<1645:R,A}
nlv{m<2381:A,A}
vfm{x>1711:xhf,A}
qcx{x<1734:A,s>767:R,m<3778:R,R}
mcn{m<2714:R,s>2638:A,R}
bv{m<3657:A,kxg}
lh{a<672:jqj,s>1629:tt,x<2340:vnp,vkl}
vkl{m<3581:jh,s<796:fdr,A}
cb{s>2842:A,A}
pfs{x>3152:R,R}
kkx{a<1765:vc,m<3453:qbp,A}
rzg{x>2274:R,x>961:nk,A}
ggp{m>3181:cbp,s>3552:A,s<3419:kxt,tcl}
gh{s<2520:fz,lg}
kxm{m<1184:R,s>1167:R,x>1873:R,A}
kq{a>2544:gtj,a<2307:dr,kqg}
hfv{a<3097:A,A}
kqg{m>2533:nzg,a<2434:kvs,dpr}
msp{s>3087:R,m<3385:R,x<1445:A,R}
zxk{x<1361:R,m<2435:R,s>1703:R,R}
zgv{m<2324:A,A}
cr{x>3701:A,a<3546:R,m<1509:A,R}
mqz{x>3102:R,x>2534:A,a>536:A,A}
bf{a<3215:A,A}
kt{m>2869:A,mjx}
hxp{x<477:A,s>3711:A,s<3501:gp,pfp}
dbl{m>3481:R,R}
kxg{x<342:A,x>554:R,R}
pj{x<2103:A,R}
ms{s<3656:A,A}
ml{a>2584:A,m>3656:A,a<2395:A,R}
xml{x>2585:svx,s<1148:rll,x>978:xz,A}
tsd{x>3459:mdj,kt}
jtz{m>3523:A,m>3510:A,x<1253:A,R}
sgx{x>2909:A,a<574:A,A}
rs{a>1460:A,R}
fp{m<3410:A,a>2356:A,s<3292:A,R}
dsx{x>2348:A,R}
kp{s>369:txh,s<230:mr,cck}
zps{x>3185:jjc,m>2419:A,a<1023:A,mb}
cpd{m<708:R,a<1615:A,s<2235:R,A}
rng{x>3076:xv,lb}
tzh{s<1231:A,s<1741:R,a<566:A,A}
qg{a>519:R,s<1366:R,s>1955:A,A}
df{a<3076:ft,m>3088:lc,a>3508:bl,dd}
vcv{m<3819:R,m<3886:R,A}
bz{a<639:R,A}
qvj{m>3958:R,m<3906:A,x>237:A,A}
djx{a<1392:rx,zrd}
qcc{x>2642:A,x<2334:R,x<2475:R,R}
rt{s<366:A,a<1565:A,s<509:rbg,A}
bs{x<2022:A,a>2687:A,R}
mbk{a>2212:A,x>510:R,A}
bj{m>2364:R,x<1648:A,A}
jjs{x>2320:A,m>3263:A,a<534:R,A}
pmq{m<3902:R,m>3939:A,A}
nt{x<2756:R,bf}
dd{s>1196:hrl,tnh}
fhn{a>1403:R,m<2367:A,R}
fjr{x<423:R,x>721:A,R}
mtt{a<3052:A,m>3202:A,x>3120:hfv,qlz}
dpr{s>3125:pxn,m>2337:sg,a>2501:R,R}
ltj{a>2818:vt,a>2673:fm,bzx}
gtj{s>3180:nfv,a>2752:rq,bk}
zp{s<921:jql,A}
tcl{s<3498:R,m<2470:A,x>2834:A,R}
kgv{s>1818:tg,pnr}
vxj{s>2128:A,R}
pqn{m>1363:R,R}
rv{m<2513:A,R}
lbb{x<2057:R,A}
pdh{s<3207:pvf,a>3332:gsf,tn}
brq{a<2554:A,s>2729:R,x>474:R,vvv}
qbp{m<3317:R,x>2791:A,s>2568:A,R}
tz{x<1963:A,pbl}
qtm{a>2403:A,A}
kzv{x>303:R,m<3672:R,a>2773:R,A}
xkv{a>2516:A,s<3402:gz,x>2893:A,dsx}
pnl{s<2996:R,R}
rqd{x<914:A,nzm}
fm{m>3402:A,x<1724:A,s>3387:A,R}
cj{x>2322:zbr,A}
qc{x<1903:A,a>775:A,x>3086:R,R}
ntt{a<3650:A,a>3786:A,R}
qkd{x<2751:lj,x>3259:kd,xg}
tg{m<3486:R,R}
dh{m<1089:A,A}
fj{a>2561:A,a>2327:A,R}
dq{s<734:kp,zdf}
cdj{a>823:R,x<2382:R,R}
kst{a>396:R,a<364:A,x<2300:R,A}
hb{m>2334:lt,s<3840:ktr,qcc}
qjf{s>1688:fv,mm}
hsh{a<1505:A,x<725:R,R}
jk{m>2673:gm,m<2405:ks,kh}
xch{x>1968:R,mmm}
ls{a>2958:jk,m<3177:kq,x>686:tdj,nfj}
nh{a>574:lq,m<883:A,a<290:jhk,pqn}
jqj{x>2431:A,x>920:A,m<3641:dt,vkc}
zmv{a>2792:jr,m<3875:nzj,qvj}
dxg{x<1343:nb,m<3417:vng,dnc}
dl{a<2671:vzn,m>3625:zmv,x<268:pz,jdz}
vj{m>3306:A,m>3227:A,a>3792:cf,nd}
nb{a<1112:zxb,s<2248:fht,s<3263:gnk,fgq}
pl{m<2553:R,a>673:rhf,sfg}
sl{x>3478:R,s<2643:cdv,m<2167:mbj,R}
gv{x>2571:R,a<3763:rjz,a>3873:ds,R}
nfl{x>2198:dps,x>1011:nm,jbv}
gnk{a<1448:R,A}
jlz{m<3118:pv,x<3042:kkx,mfc}
gsf{m<2991:qkd,xh}
bc{a<3532:R,s>3672:R,R}
xk{x>1279:A,R}
pt{m<3624:A,A}
mfp{s>2223:R,m<2159:A,R}
gr{x>1000:A,m>1123:A,a<3674:A,R}
qf{x<2406:R,A}
vjg{m>2489:fgp,x<883:dld,xb}
bqd{x<2342:R,R}
dgh{s>3158:A,A}
fpl{a>355:kbj,a>315:qq,a>283:pt,xjs}
tp{s<1022:R,s<1303:R,stv}
gbb{x>93:R,s<3604:A,s>3762:A,R}
scv{s>3457:tzp,m>3390:A,x<940:hn,A}
sb{s<3197:R,R}
qjj{m<3687:R,x<354:A,a<2602:A,R}
knz{x>489:R,A}
kcs{a<1255:A,s<2138:A,m<3653:gdz,A}
nzj{s<3579:A,s>3737:A,A}
bh{m<3599:R,a>762:A,R}
xv{s>3395:A,a<253:A,s>3101:R,R}
nz{m>2300:pg,a>2260:grx,A}
rl{s<1583:A,s>2096:A,x<1641:R,A}
vrp{x<1523:A,a>2612:sbv,A}
dld{m>2302:sc,x>423:A,vxj}
rpp{a<1156:qf,s>1304:ss,ksz}
lcv{m<2081:R,x>635:A,R}
rqx{s>2365:A,mh}
dmf{m<1573:R,m<1717:A,a>3749:R,R}
ln{m<3734:A,R}
nfj{s>3059:dl,a>2458:zjx,m<3559:fnl,cz}
fh{x<2319:ljl,A}
qlz{s<3900:A,R}
ltz{x<327:A,a<2929:R,m<3698:R,A}
nzt{s<2483:R,hf}
pjk{s<1064:A,a<1601:A,A}
lqd{m>3441:zm,x>1635:R,a<732:hr,R}
xm{m>3148:A,kn}
mlm{x<1457:R,x>2468:A,A}
hfl{x<1163:A,R}
nr{m>3825:A,m<3716:R,m<3780:R,A}
lm{x>3142:A,A}
shl{x>1610:md,s<3070:gcr,s>3456:dtr,vrp}
xh{s<3575:bp,a>3690:nf,tpk}
cq{a<3251:A,x>1657:R,x<700:zzl,tv}
dp{x<2035:mfj,s>2712:rng,rds}
svs{a>648:dbj,pxx}
br{x>1376:R,R}
sps{a<2429:A,m<3739:A,A}
ft{m<2705:psj,a<2763:nfl,hq}
fll{m<2484:R,x<2065:R,A}
lrk{a>584:R,x>2133:mqz,R}
xjs{m>3597:A,A}
jgv{m>2980:vq,s>3724:hb,xkv}
zr{s<2878:A,a<2521:R,s>2955:R,R}
cz{m>3732:zn,a>2334:bv,cbk}
mdj{s<624:txx,a>1835:vgh,x>3783:A,zrx}
hrl{a<3223:lk,cl}
sk{s<2979:R,A}
vfz{a<3876:A,x<738:R,x<1187:A,R}
hf{x<1635:R,m>1245:R,R}
cf{x<3619:R,s<1482:R,m>3152:R,A}
xc{a>3566:spr,s>868:nlv,cd}
sr{m<2311:mfp,m<2503:sgx,s<2472:tzh,R}
jvx{a<3643:R,s>1130:A,s>726:R,A}
qq{a<335:R,m<3739:A,s<921:R,A}
rcn{a>1642:cs,m>2904:dxg,pkb}
sg{x<857:A,a>2495:R,m>2405:A,R}
dn{s<2869:A,a<2239:R,R}
lcn{x<1209:A,a<2189:rdc,x>1572:dgh,br}
kh{s>3091:qvb,a>3439:ph,kx}
pk{a<2811:R,vl}
fzj{a>762:R,m<3771:R,R}
nzm{x<1856:A,R}
thc{a>671:R,x>893:R,m<2536:A,A}
hzc{a>731:sxq,dbx}
qh{m>3487:rzg,x<2346:ttb,x>2986:vj,gv}
djg{x<1541:R,A}
dds{x>1478:A,A}
hgr{s<3322:A,m<2974:A,A}
dc{x<3545:A,x<3753:A,x<3903:R,R}
tdj{x<1370:zgx,m>3549:shl,xtm}
xq{s<2961:A,a<2702:qjj,A}
hn{x>800:R,A}
tsq{s>2129:A,A}
md{x>1708:gtb,A}
bl{a>3676:hm,xc}
cck{x>1825:R,a<3319:R,s<298:A,gr}
km{m>2487:kfx,m<2299:R,x<1133:R,gs}
rbg{m<737:A,a>1624:A,R}
stm{m>1640:R,m<1309:A,R}
mn{m>3023:A,m<2890:A,R}
pd{m>3519:A,a>1781:R,A}
gqp{x>2620:A,A}
fx{a<3599:R,a>3604:R,x>2471:A,R}
jxv{m<3906:R,a>767:A,R}
xx{m>2804:A,cfz}
rll{s>544:A,a>159:A,R}
jql{x<1710:A,R}
rtl{s>1295:R,a<608:A,R}
qnv{s>2839:A,m>3403:R,x<278:A,R}
gf{a>3286:R,m>3448:R,R}
bqc{a<691:mrp,A}
pz{m>3384:dbl,x>144:ms,m>3289:gbb,R}
fnk{m<3387:jjs,a<555:mlm,m>3441:rtl,R}
nv{s<2747:R,x<269:A,x<323:A,R}
xg{x>3075:pqg,m>2409:rz,m>2164:R,A}
lnx{a<2455:R,s<3074:R,R}
jzq{s>3325:R,s<2876:kc,R}
sfg{x>208:A,x<139:A,A}
rjz{s>891:R,s<564:R,A}
sz{a<1723:gl,x<1494:rh,s<2041:R,kmj}
nqv{a<681:sr,m>2406:kfl,x>2455:sl,xch}
xgh{s<2493:df,x<1826:ls,pdh}
zm{s>1351:A,s<563:A,R}
gc{x<1987:A,x>2889:A,R}
sc{a>1263:A,A}
tzf{x>1092:vp,x<715:hs,A}
rfb{s<2935:A,A}
ph{m>2501:A,x>626:A,jtr}
bdc{s>2076:A,A}
psj{s>1402:bs,fh}
lf{a<1564:sbc,hgq}
rnd{s>422:A,s<277:A,x>596:A,R}
pf{a<1465:R,x<3179:cpd,x<3627:R,qjn}
kl{a<1327:vk,a>1664:tb,a>1500:prn,djx}
dgg{m<3199:R,x>2626:A,R}
hs{x<437:A,s>3167:A,R}
fht{s<1326:rs,a<1403:R,R}
vc{m>3660:A,R}
xgj{m<3317:sb,x>1605:fp,dmd}
mbj{x<3057:R,m<2089:R,R}
tb{a<1942:tp,m<1218:scb,frc}
bn{x>2462:R,m<3292:R,m<3337:R,A}
ktr{a>2601:A,m<2177:R,R}
cbk{s<2765:gd,s>2959:tqz,dn}
ff{a>3714:R,A}
rz{x>2911:A,R}
jpz{a>2910:A,hsb}
rq{x>669:jgj,rfb}
pqx{s<2313:A,s>3278:R,R}
dk{m>3317:R,x<258:A,R}
vv{x>492:R,x<254:A,x<396:A,R}
pbx{m<931:A,a<1287:R,R}
mqt{m>3717:R,x<268:A,a<2869:A,A}
kbm{a>3143:ggp,s>3735:mtt,jnb}
jnt{m<3314:vqs,x>591:hgz,zx}
bbh{s<2984:R,A}
sxl{s>3614:dds,qt}
llq{a<2592:qtm,A}
ck{x<158:A,nv}
cd{a>3531:djg,A}
fgp{x>892:tcj,fjr}
qp{m>512:A,R}
nc{a<474:vzs,m<3190:bg,m>3492:pq,svs}
svj{s<2449:A,x<3504:A,x<3675:lcx,R}
lj{s<3627:A,x<2338:zgv,A}
ngk{x<1497:A,s<3064:R,A}
jgj{m<2559:R,m<2903:R,R}
jdz{a<2815:rc,m<3371:cc,R}
lgd{m<2393:R,R}
pfp{x<766:R,x<955:R,a<631:A,R}
rh{m>1085:A,m<377:R,m>618:A,A}
kvm{m<3573:R,s<2902:R,R}
qcs{x>2830:bjk,x<2257:R,x<2558:A,A}
xhf{x>2614:A,m>2750:A,m>2405:A,A}
pch{x>1502:dmf,stm}
mrp{x>1044:R,x>905:R,a<607:R,R}
zdp{a>2501:R,m<3592:R,x<274:R,A}
jg{m>3318:R,a>979:R,a<923:R,R}
pxs{s>2752:A,R}
rds{m>3000:R,nj}
gcx{s<2743:R,m<3550:A,R}
kfx{x>1151:R,s>1153:R,s<456:A,A}
cbp{m>3589:R,x<3159:A,x>3716:R,A}
dpb{a<838:nc,rcn}
dzn{x<1449:R,A}
vk{m>1279:mf,hv}
gkq{m>3670:R,x<2267:A,R}
lq{a<1006:R,A}
dbx{s>882:sfp,R}
pbl{a>674:R,x>2988:A,x<2550:A,A}
nfg{a<809:A,a<1149:R,a<1336:A,A}
fl{x<3047:A,a<817:A,a>1217:R,R}
zrd{a<1462:R,s<768:R,s>1204:A,R}
lb{s<3178:A,A}
gcr{x<1500:dzn,s>2689:nfr,s<2613:A,A}
pxx{s>2428:lrk,fnk}
nf{a>3889:cpr,rxr}
ftm{x<2088:A,s<3057:R,m>3705:A,A}
rhf{s<2865:R,A}
fnl{a<2261:rr,x<436:msl,jnt}
zpp{a>3556:A,s>2802:A,m>2588:A,R}
mg{a>777:jfc,a>704:jlq,tz}
nm{s<1218:R,s>1893:R,m>3296:ppl,px}
zx{a>2338:A,A}
jr{m>3845:R,A}
dcc{m>3019:vn,a>546:R,x<2655:hpz,dmh}
grx{m<2109:R,A}
dfj{s>3487:kk,pnl}
fb{m<3548:A,x<2510:R,a>3239:A,R}
sxq{m>3850:jxv,a>782:qcx,s>912:R,fzj}
hh{m<3013:R,a>2518:R,x<479:R,R}
xb{s<2626:R,m<2270:A,s>3239:R,tcv}
lg{x<1194:A,x>1978:R,x>1486:R,A}
dmd{m>3453:R,m>3384:A,m>3354:A,A}
zh{m>2953:zhx,s>2342:A,a>812:cdj,gkm}
zbr{a>3239:R,A}
sxx{m<3616:A,x>2642:A,R}
gkm{x>2141:R,s<1253:R,a<791:R,R}
bzx{x<1746:R,x<1797:R,R}
kc{a<3559:A,A}
sh{s<1259:A,A}
cbj{m>2350:A,s>1743:A,x>2193:A,A}
kbj{x<1463:A,a<430:A,A}
pq{m<3722:lh,a<658:qkx,s>2237:mg,hzc}
kn{m>3080:A,s>2891:R,R}
crj{a>3362:hmr,m<2623:bj,A}
hgz{a<2374:R,A}
jp{m<3555:R,m<3812:R,A}
txp{a<2430:R,A}
pnr{a<3235:R,A}
svx{x<3299:A,a<145:A,R}
pg{x<1139:A,R}
tqz{s<3020:R,m<3664:A,a>2254:A,A}
xl{s<3325:A,a>568:R,R}
dt{x>339:R,A}
hr{a<701:A,A}
mpc{a>745:R,A}
zxm{a<3391:A,x<536:A,A}
sq{x<984:R,m>2584:A,R}
lc{a>3466:qh,x<1943:fs,jx}
cc{a<2872:A,R}
lk{a<3173:zxk,s<1745:dkc,bdc}
fdr{x>3434:A,s<310:R,A}
kbz{x>2565:A,pj}
zd{m<3116:R,x>1333:R,R}
kxt{a<3259:A,s<3305:A,R}
lt{a>2612:R,s<3820:A,R}

{x=1209,m=1881,a=534,s=1202}
{x=843,m=38,a=449,s=28}
{x=551,m=469,a=876,s=2049}
{x=533,m=893,a=14,s=102}
{x=32,m=665,a=681,s=44}
{x=349,m=129,a=334,s=1073}
{x=181,m=664,a=9,s=2721}
{x=2191,m=221,a=25,s=2958}
{x=334,m=574,a=1927,s=1045}
{x=1795,m=190,a=118,s=110}
{x=165,m=903,a=1279,s=48}
{x=1616,m=716,a=221,s=648}
{x=2469,m=467,a=591,s=585}
{x=551,m=1260,a=2679,s=1278}
{x=571,m=923,a=197,s=129}
{x=353,m=2319,a=7,s=2787}
{x=3073,m=999,a=1771,s=762}
{x=305,m=527,a=678,s=1400}
{x=1135,m=315,a=29,s=1067}
{x=2169,m=454,a=1320,s=789}
{x=1043,m=1463,a=399,s=797}
{x=150,m=1914,a=1230,s=325}
{x=1028,m=460,a=1520,s=42}
{x=1170,m=866,a=64,s=579}
{x=1203,m=1692,a=978,s=461}
{x=1359,m=436,a=2559,s=555}
{x=368,m=762,a=2064,s=173}
{x=803,m=338,a=1090,s=975}
{x=182,m=3161,a=2059,s=2030}
{x=12,m=1182,a=1575,s=1581}
{x=340,m=1727,a=1030,s=588}
{x=51,m=90,a=480,s=352}
{x=52,m=1256,a=15,s=80}
{x=1146,m=587,a=1361,s=657}
{x=8,m=2994,a=1013,s=2490}
{x=2446,m=3523,a=1289,s=220}
{x=14,m=460,a=855,s=89}
{x=2034,m=170,a=1527,s=182}
{x=2072,m=58,a=379,s=181}
{x=729,m=57,a=1534,s=530}
{x=160,m=395,a=1470,s=2}
{x=831,m=952,a=1548,s=161}
{x=682,m=1256,a=1672,s=1619}
{x=1520,m=1552,a=531,s=1526}
{x=1020,m=1125,a=44,s=434}
{x=628,m=490,a=2193,s=1115}
{x=582,m=610,a=539,s=380}
{x=2496,m=446,a=2165,s=101}
{x=104,m=742,a=1065,s=2977}
{x=1669,m=999,a=1931,s=2973}
{x=13,m=830,a=8,s=151}
{x=39,m=1177,a=2976,s=423}
{x=1051,m=75,a=1578,s=187}
{x=38,m=519,a=328,s=35}
{x=5,m=722,a=698,s=309}
{x=492,m=3698,a=917,s=1024}
{x=1388,m=1230,a=721,s=347}
{x=585,m=65,a=129,s=2343}
{x=111,m=315,a=186,s=1485}
{x=234,m=2107,a=26,s=1061}
{x=280,m=1036,a=2212,s=94}
{x=268,m=590,a=20,s=1558}
{x=1918,m=419,a=200,s=1538}
{x=1528,m=1076,a=1978,s=1253}
{x=846,m=930,a=2340,s=439}
{x=313,m=1529,a=647,s=125}
{x=937,m=1739,a=1897,s=741}
{x=52,m=410,a=448,s=2164}
{x=1435,m=714,a=554,s=1286}
{x=533,m=1067,a=697,s=1498}
{x=27,m=373,a=1334,s=1056}
{x=1709,m=80,a=337,s=649}
{x=1587,m=415,a=2096,s=251}
{x=1582,m=2201,a=48,s=885}
{x=1506,m=1540,a=230,s=494}
{x=46,m=347,a=804,s=158}
{x=748,m=76,a=456,s=968}
{x=532,m=921,a=874,s=811}
{x=3337,m=152,a=1074,s=22}
{x=188,m=623,a=10,s=865}
{x=12,m=1095,a=1734,s=759}
{x=66,m=16,a=1701,s=25}
{x=251,m=2458,a=2209,s=506}
{x=2322,m=2027,a=677,s=814}
{x=1142,m=2788,a=515,s=132}
{x=148,m=106,a=26,s=122}
{x=176,m=179,a=11,s=272}
{x=2239,m=130,a=500,s=29}
{x=2729,m=690,a=903,s=686}
{x=27,m=26,a=65,s=147}
{x=3080,m=2118,a=2037,s=716}
{x=967,m=161,a=1584,s=789}
{x=2175,m=1456,a=370,s=1131}
{x=198,m=1207,a=1139,s=532}
{x=498,m=305,a=640,s=344}
{x=641,m=3506,a=488,s=89}
{x=2691,m=845,a=2001,s=523}
{x=520,m=776,a=25,s=505}
{x=336,m=838,a=152,s=184}
{x=591,m=38,a=1840,s=612}
{x=71,m=150,a=1312,s=755}
{x=2400,m=2429,a=3492,s=3478}
{x=108,m=3175,a=695,s=653}
{x=992,m=72,a=6,s=20}
{x=980,m=546,a=2379,s=1383}
{x=195,m=1375,a=1375,s=751}
{x=1224,m=1914,a=1683,s=751}
{x=26,m=725,a=649,s=798}
{x=3519,m=194,a=868,s=471}
{x=593,m=941,a=213,s=312}
{x=97,m=1307,a=1090,s=2296}
{x=1382,m=400,a=810,s=96}
{x=1445,m=627,a=1946,s=162}
{x=454,m=25,a=136,s=824}
{x=3503,m=2619,a=1773,s=263}
{x=729,m=1026,a=227,s=187}
{x=3793,m=2727,a=1030,s=3067}
{x=475,m=915,a=1558,s=878}
{x=694,m=2753,a=2509,s=214}
{x=735,m=772,a=545,s=503}
{x=1785,m=1122,a=997,s=1511}
{x=1308,m=200,a=752,s=1747}
{x=1132,m=424,a=2250,s=173}
{x=366,m=225,a=1893,s=2041}
{x=64,m=520,a=554,s=1792}
{x=1713,m=1242,a=184,s=362}
{x=245,m=785,a=677,s=274}
{x=1282,m=198,a=1110,s=2016}
{x=1388,m=2657,a=745,s=1920}
{x=1343,m=419,a=946,s=874}
{x=1594,m=638,a=2829,s=155}
{x=144,m=3710,a=350,s=3109}
{x=867,m=400,a=190,s=975}
{x=899,m=1278,a=2143,s=3462}
{x=182,m=455,a=426,s=976}
{x=126,m=76,a=1766,s=346}
{x=2409,m=588,a=729,s=3765}
{x=2297,m=1079,a=12,s=391}
{x=601,m=233,a=633,s=1157}
{x=766,m=1102,a=311,s=2170}
{x=2119,m=712,a=2509,s=214}
{x=813,m=971,a=139,s=1020}
{x=44,m=2286,a=125,s=88}
{x=69,m=2531,a=45,s=133}
{x=401,m=157,a=2074,s=353}
{x=671,m=242,a=3808,s=1449}
{x=159,m=766,a=148,s=3312}
{x=329,m=2706,a=315,s=1438}
{x=850,m=857,a=337,s=56}
{x=565,m=433,a=818,s=2920}
{x=139,m=2318,a=188,s=1233}
{x=25,m=1360,a=666,s=325}
{x=315,m=388,a=1231,s=988}
{x=81,m=980,a=355,s=40}
{x=1023,m=1164,a=1402,s=576}
{x=1945,m=2437,a=3,s=1583}
{x=153,m=557,a=1399,s=201}
{x=2402,m=254,a=76,s=1145}
{x=993,m=778,a=836,s=1066}
{x=1896,m=19,a=3189,s=2458}
{x=1025,m=1291,a=831,s=1412}
{x=640,m=585,a=433,s=372}
{x=493,m=2359,a=968,s=1746}
{x=2942,m=2698,a=332,s=1472}
{x=66,m=2892,a=1975,s=61}
{x=1620,m=442,a=2394,s=1208}
{x=255,m=339,a=1037,s=2815}
{x=2902,m=985,a=423,s=2649}
{x=179,m=60,a=387,s=198}
{x=189,m=2861,a=89,s=2606}
{x=1341,m=232,a=1874,s=2003}
{x=809,m=995,a=2135,s=150}
{x=1217,m=407,a=1047,s=1505}
{x=1821,m=774,a=710,s=2784}
{x=3041,m=948,a=93,s=9}
{x=2189,m=2156,a=3100,s=175}
{x=2642,m=517,a=139,s=1983}
{x=121,m=3103,a=1953,s=59}
{x=190,m=236,a=7,s=1521}
{x=843,m=1662,a=613,s=1288}
{x=3337,m=76,a=644,s=66}
{x=590,m=83,a=1317,s=2773}
{x=74,m=369,a=6,s=12}
{x=36,m=505,a=1415,s=15}
{x=3246,m=55,a=1748,s=2441}
{x=3265,m=23,a=952,s=63}
{x=896,m=743,a=168,s=48}
{x=12,m=1583,a=576,s=516}
{x=924,m=300,a=1088,s=1306}
{x=441,m=2258,a=1242,s=847}
{x=2483,m=38,a=2126,s=554}
{x=589,m=793,a=640,s=73}
{x=530,m=130,a=208,s=140}
{x=384,m=478,a=742,s=3473}
{x=2287,m=2872,a=631,s=1947}
{x=125,m=1581,a=515,s=1560}
{x=1880,m=646,a=2302,s=258}
{x=1478,m=255,a=150,s=2157}
{x=66,m=664,a=245,s=2546}
{x=1970,m=2533,a=1243,s=709}'''

TEST_INPUT = '''px{a<2006:qkq,m>2090:A,rfg}
pv{a>1716:R,A}
lnx{m>1548:A,A}
rfg{s<537:gd,x>2440:R,A}
qs{s>3448:A,lnx}
qkq{x<1416:A,crn}
crn{x>2662:A,R}
in{s<1351:px,qqz}
qqz{s>2770:qs,m<1801:hdj,R}
gd{a>3333:R,R}
hdj{m>838:A,pv}

{x=787,m=2655,a=1222,s=2876}
{x=1679,m=44,a=2067,s=496}
{x=2036,m=264,a=79,s=2244}
{x=2461,m=1339,a=466,s=291}
{x=2127,m=1623,a=2188,s=1013}'''


class Part:
    def __init__(self, part):
        x, m, a, s = list(map(int, re.findall(r'\d+', part)))
        self.x = x
        self.m = m
        self.a = a
        self.s = s

    def __getitem__(self, item) -> int:
        match item:
            case 'x':
                return self.x
            case 'm':
                return self.m
            case 'a':
                return self.a
            case 's':
                return self.s
        raise KeyError(f'{repr(item)} not found.')

    @property
    def value(self) -> int:
        return self.x + self.m + self.a + self.s


class Rule:
    def __init__(self, rule: str):
        system, op, count, result = re.match(r'([a-zAR]+)([<>])?(\d+)?[:]?([a-zAR]+)?', rule).groups()
        self.system = system
        self.op = op
        self.count = int(count) if count else None
        self.result = result
        self.rule = rule

    def get_next(self, part: Part) -> str | None:
        if not self.count:
            return self.system
        check = part[self.system]
        if self.op == '>' and check > self.count:
            return self.result
        if self.op == '<' and check < self.count:
            return self.result
        return None

    def __str__(self):
        return f'{self.system}{self.op}{self.count}:{self.result}' if self.count else self.system

    @property
    def index(self) -> int:
        return 'xmas'.index(self.system) if self.count else -1


class Workflow:
    def __init__(self, workflow: str):
        name, flow = re.match(r'([a-z]+){(.*?)}', workflow).groups()
        self.name = name
        self.flow = flow
        self._rules = list(map(Rule, flow.split(',')))
        self.last = flow.split(',')[-1]

    def get_next(self, part: Part) -> str:
        for rule in self.rules:
            if next_flow := rule.get_next(part):
                return next_flow

    def __str__(self):
        print(f'{self.name}={",".join(map(str, self._rules))}')

    @property
    def rules(self):
        yield from self._rules


def solve_combination(input_: str) -> int:

    def evolve(part, item):
        new_row = list(row)
        new_row[part] = item
        return new_row

    flows = {flow.name: flow for flow in map(Workflow, input_.split('\n\n')[0].splitlines())}
    rows = [('in', [range(1, 4001)] * 4)]
    accepted = 0
    while rows:
        name, row = rows.pop()
        if name == 'A':
            accepted += np.prod(list(map(len, row)))
            continue
        if name == 'R':
            continue
        flow = flows[name]
        for rule in flow.rules:
            if not (num := rule.count) or num not in (r := row[rule.index]):
                continue
            op = rule.op == '>'
            splits = [r.start, num + op, r.stop]
            new_ranges = range(*splits[:-1]), range(*splits[1:])
            rows.append((rule.result, evolve(rule.index, new_ranges[op])))
            row[rule.index] = new_ranges[not op]
        rows.append((flow.last, row))
    return accepted


def solve(input_: str) -> int:
    flows, parts = input_.split('\n\n')
    accepted = 0
    flows = {flow.name: flow for flow in map(Workflow, flows.splitlines())}
    parts = map(Part, parts.splitlines())
    for part in parts:
        flow: Workflow = flows['in']
        while (next_flow := flow.get_next(part)) not in ['A', 'R']:
            flow = flows[next_flow]
        if next_flow == 'A':
            accepted += part.value
    return accepted


if __name__ == '__main__':
    part1_args = []
    expected_1 = [(19114, [TEST_INPUT, *part1_args])]
    func_1 = solve

    part2_args = []
    expected_2 = [(167409079868000, [TEST_INPUT, *part2_args])]
    func_2 = solve_combination

    if expected_1:
        for idx, (e_total, e_params) in enumerate(expected_1):
            solve_problem(func_1, 1, (idx, e_total), *e_params)
        solve_problem(func_1, 1, None, INPUT, *part1_args)

    if expected_2:
        for idx, (e_total, e_params) in enumerate(expected_2):
            solve_problem(func_2, 2, (idx, e_total), *e_params)
        solve_problem(func_2, 2, None, INPUT, *part2_args)