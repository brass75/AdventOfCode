import re
import time
from collections import defaultdict

INPUT = """fzl-,tcjp=8,vkjr=9,xs-,jktcpk=3,gzp-,kfsxsd-,zxkv=7,fxz-,pj=7,mhbdch=7,xlss-,smk-,ppz-,kqggd-,dqh=7,gmv=6,
tjjfm=2,gbv=5,gn-,ld=7,jdr-,phq=3,rd-,qz=3,sh-,gzsb=2,glrt=7,vjkrjg-,gjqmpc=7,qnx=7,mf=1,tnrm-,lppg-,gnvx=1,rv-,vnt-,
bst-,gkb-,tl=1,bggff-,lm=8,mqq=7,hr-,gkb-,fspkn=2,tjjfm-,shshb=3,qfczq-,zk-,zcsc-,lnrjh=2,fz-,bkb-,rg-,bcfzn=6,
xsbb=5,sm=3,rqs-,rvlv=9,pvh=9,rl-,zrb=9,lftk=1,cdn-,zp=8,hc-,mf-,hp-,zk-,dbj=5,tm=9,zx-,gmp=4,gcq-,mxq-,lvh-,lkhb-,
vn=9,gzsb=6,xlss=9,drkhc=8,rgqg=1,hkr-,fxz=7,xsm-,fvmf=4,hsm=7,dlrss=9,rv-,kj-,ndtc-,zjf-,zj=9,kv=5,sxvv-,hj-,mltm-,
qggz-,mntr-,td=5,lppg=1,xqb-,brt-,nm-,vlp=7,zcjnv=6,chh-,dd=2,fh-,hxfkx=6,hj=6,rzk=7,skpq-,rxb=1,fn=1,nc=1,vqq-,ndq-,
xtgd=6,qlgv-,dl-,xln-,rqs=5,vpmmf=1,llvv-,hzp=6,dnbql=3,rqz=5,nfhb=7,vdb-,gmp-,hskv-,xs-,vk-,xll-,ng=2,xb-,mjjph-,
tss-,lsd-,qsj-,tbdb-,tdnm=6,bv-,qz=5,zp=8,jn-,fh-,dqh=1,rgrd=5,kqggd-,ddccc-,gdx=3,br-,cnb=4,tfx-,scp=5,rgch-,
xltvn=4,xdblmh-,jdr-,fz-,crd-,hfr-,xlss=2,fxz=5,rzl-,vdb-,tss=6,kc=2,bdmrg=6,mkv-,hdr=9,pv-,qcr=4,ntxqq-,mhbdch=8,
npghs-,jb-,lzcp=1,zbl-,vsjs-,dmv=1,zhc-,tfx-,jc=8,vlhhb-,zcbg=2,fcbzpl=8,gkb-,zppn-,jj=6,xlc=6,xltvn-,cnb-,lftk-,
ptmc-,fxz=6,ncn-,gzp-,lgtd=4,znp-,ncn=8,fg-,lnrjh=6,lkhb-,tnrm=4,hkr-,ltc-,lv-,ck-,dn=5,srt-,hk-,fspkn=9,drnvhj=5,
gvf-,gzp-,pq-,lbq=8,lm-,lsx-,jf-,vkjr-,lcvzfp-,vqqp-,glrt=7,zx=4,hskv=9,bqm=6,jm=6,tshhq=7,sg-,pq-,rgqg=4,bcpb-,df=4,
qpqx=6,fn=7,drnvhj=5,vf=8,zsx-,jbd-,kczn=9,fspkn=1,cjd=5,hzp=1,zpkc-,kczn=7,mrd=9,ndq-,hp=4,nfmf-,npghs-,zvd=9,dt=2,
jdf=2,xzq-,xb=7,cpbb-,nd-,sgq=2,fc=1,tdnm-,fvmf-,ncn=4,zrdk=1,bvb-,gmp=2,pvh=2,klzj=7,lqlh-,tgm-,vf-,xll=3,lcvzfp=4,
jrp=1,jq-,cjd-,nxqhqd=9,lx=4,ltc-,kc=9,gddghs=4,lj=9,bggff=8,pxk-,glgpxh-,mrd=6,mhkbd=1,lbq-,rgch-,vf-,ks=8,dt=5,
tb=2,cdn=3,vlxv=6,rgrd-,mcfh=9,bkg-,fd-,bdz=4,vk=7,phd=4,bkg-,krz=6,flk=1,jf=8,zxkv=2,hdhk-,nxqhqd-,dvgz=7,dbj-,rvc-,
fshfd=7,tb=4,mjx-,vnsgg=1,zppn=6,zx-,kk=2,xs-,xprp=7,hh=9,xnp=8,vndj=9,qnzlf=3,bdmrg-,dxl=5,ss=4,clv-,hk=3,kgx-,
qqvmc=9,xzq-,kfsxsd-,bdt-,vqq-,lqlh-,jvp=7,tshhq=5,pvh=4,cp=4,bpd-,bqql-,dvx=8,qtql=7,zxkv=3,qfv-,xlss-,lzs-,kt=3,
ltsb-,pfs=2,dmv-,qcr-,sl-,qsjch-,hmd-,bcpb-,drnvhj=4,bf=3,qx=1,gddghs-,zcjnv-,bdmrg-,rd-,ddccc=2,hvk=6,kk=1,chh=5,
mxq=9,kcq-,vkjr-,ntxqq-,glgpxh=6,dvzlc-,lnt=2,rkk-,mzpgh=7,pl-,vndj-,nc-,xx=5,klzj=2,xhs-,cx-,jz=7,rmh=7,gjqmpc-,
zdr=4,csqh-,zppn-,zc-,bvb=4,tjjfm-,rdzzjm=8,dbj-,sr=4,npghs=1,pxs-,blxq-,rqz=1,grxx-,sg-,fqmdgn-,jf-,pqjf-,xzljl=9,
zdr-,hh-,cnb=5,jrq=1,dvx=2,pzbsd-,xpm=5,znp-,gqsr=2,qtql-,kssg=4,qm=3,scd=1,lzcp=4,gdx=9,shshb=2,sxmq=2,mtqb-,xn-,
xln=4,vv-,nj-,tjjfm=7,rp=5,kcq=3,bcfzn-,dbj=9,zcbg-,bfx-,gvf=2,ptmc=7,jb=7,kv-,znl=5,gsk-,zjf=8,kmx-,rbft=1,csqh-,
zp-,rq=1,rrx=9,mh=2,gnvx=9,mqq=9,bqql=6,gj=2,mhv=3,dcc-,kgx-,vhrd=6,ztj=2,ng-,rl-,bqm=1,rgqg=6,blmgvg=5,jx-,vqqp=8,
jb-,lnk=2,rvlv=9,tz-,hj-,ltc=7,gcjgs=7,tm=2,mn=4,ss=7,vlhhb=4,hkd-,xf-,ltsb-,rzl=7,zx=5,phq=8,srt-,jvp=5,sgq-,
qnzlf=9,lsd-,fbrz-,dsnd=3,hj-,tcjp-,vnsgg=9,xn-,mzpgh-,sxvv-,gjqmpc-,ncn-,mqq=2,tmpd-,rkk=6,qrlrxg-,csnq-,ltsb=6,pq-,
mjx=6,bkc-,bvb-,kgpnf=2,xv=7,cjd=6,hp=3,vf-,pg-,jnq=2,tnng=7,qq-,dxl=5,nfpqv-,rg=9,dmv-,gd-,rgch-,nfpqv=9,gjqmpc=6,
sgq-,cjd-,qnn-,ztj-,gn-,jqhg-,pzbsd-,qjn-,gggk=6,mntr=8,sxvv=3,jtx-,krz-,lzs-,pvh-,rrx=1,kgpnf-,bkg-,krz=4,vpmmf=8,
rm=5,jr-,lx-,hbsv=1,pq=4,txs=9,mltm=3,sr=1,hr=8,dqh-,rm-,vdb=8,hdhk-,fzx-,xpm=1,hkr=1,qx=3,xn=1,zjf-,bpd=7,vxb=4,
mcfh-,dcc=7,sgq-,vpmmf-,zcsc-,gggk=2,hr-,sgq-,tmpd-,rbft-,xm-,pqjf=6,vnt-,hmd-,vg-,sv-,bqm-,dsnd=2,hbq-,zc-,fxjc-,
vsjs-,xv-,jqhg=2,bqm=6,qtz-,rxb-,mjx=3,br=8,hp-,bf=8,hbq-,lnrjh=3,xb=9,cdf=4,pm-,xlc-,tm=8,jrq=1,hq-,kqggd-,dhh-,tf-,
nxqhqd-,qpqx=9,vpmmf=8,kgx-,glgpxh=2,rzl=1,qtz-,rl=5,sb=5,lfz-,bcpb-,xsdlmd=8,fshfd-,vlkx-,ss=3,xs=2,mn=5,dl-,lzcp=8,
bqql=3,nd=4,lsx-,znl-,ltc=1,qggz-,zrb-,tbdb=4,drkhc=7,dkvqm-,tz-,hvk-,ld=5,mjx-,bl=5,qx=2,zppn=7,rgrd=1,bpd=7,bdmrg-,
rl-,rqz=7,kc=1,gzp-,kcx=6,kmx-,rxptm=4,rrn=4,mhv=4,zjf-,blmgvg-,csnq-,ttgzdn-,ptmc=6,jq-,rxptm=8,mtqb=5,bpt=7,pxs-,
cx=7,cz-,mn-,qfv=5,kgv=2,xv-,blmgvg-,cp=4,hq-,vlp-,xnp-,hh-,lbrn-,crd=3,jc=2,sr=9,vkxm-,mtqb-,sf=3,sv-,hfdzfc-,gbv=3,
xsdlmd=9,nst=2,kf-,vn=4,nfhb=8,gkb-,rvlv-,drqq=5,kx=9,hp=8,dh=3,hbq-,pfxqhx=9,zx=9,jc-,zjttq-,vc-,lnk=6,tnrm=8,nxz=1,
lcvzfp-,dnbql=6,xs-,tshhq-,kgv-,dvgz-,zhg=8,ksm-,kt=4,jqhg=8,xpllk-,fspkn=6,fc=3,rbft-,scp=5,hk-,hbsv-,drqq=8,kv=6,
zlt=6,sxmq=8,qz=9,brt-,smr-,zsx=2,jvp-,vxcfp-,sf-,zhg=1,rmh=8,ztj=9,tb-,jdf-,xb=6,fvmf=5,vqq-,lm-,rlx-,zjttq-,lzcp-,
fd-,vkjr=7,hj-,qnn=1,rv-,tb=9,sfrd=7,dhh-,smk=3,xb-,glms=3,jgmsl-,xzq-,mmx=8,zcbg-,pxs=8,cz-,ksm-,skpq-,rrn-,td-,
hfr=4,pq-,vt-,krz-,crd-,dnbql=2,mmx=3,rq-,tgm-,fbrz=7,xm-,rv=1,sv-,nfmf-,pptj=7,kgpnf-,cnd=1,vdb-,sb-,pzbsd-,pqc=3,
mf=3,rm=7,cjd-,tnng-,mcfh-,fvmf=5,qsjch=5,dt-,hmd=2,hkd-,hvhd=7,nm=3,mpd-,gsk=1,cbnq=2,sl=8,zhc=8,xnp=7,jrq=8,
xzljl=1,ht-,tcjp=4,jgmsl=6,vn-,fqmdgn-,xln=4,tfx-,kfjgqb-,pv=3,dz=5,dj-,bpd=9,rqz=1,cc-,nxqhqd-,kkz=4,drqq=8,rzk=9,
skk-,tz=4,nfpqv=4,kfsxsd-,pxk-,hk-,nxqhqd=7,rdzzjm=3,dz-,xx=5,sb=6,phd-,cnk-,zqvb-,rzl-,hxfkx=9,llb=3,sr-,gsk=7,bfx-,
dmv-,qm-,lf-,jrq=3,hp=2,scp=7,mcfh=7,lnrjh=8,fvmf=2,hvk-,sv-,drnvhj-,jbd=2,hdr=8,klzj-,bggff=5,ctdr=3,bdt=2,kbl-,
tg=8,tss=3,vjkrjg=7,vhrd-,jf=1,zjf-,krz-,gd-,lkhb=8,lbrn=8,xtpn-,xhs=9,nxqhqd=6,qfv=8,grxx-,ltc-,gd=2,ctdr=3,vlhhb=2,
td=5,bdt=5,gzsb-,rrx-,njp=7,pxk=6,rq=2,lqlh-,vnsgg=8,llb-,xpd=2,zppn-,rsv=5,qn-,hbq=9,bcfzn=8,vlkx-,jqhg-,dk=9,
tbdb=9,skk=6,pqc=6,mkv=7,pqc-,bvb=6,zp-,fg=3,np=7,sxqh-,hbd=9,lhj-,fg-,lfz-,lv-,ksm=3,rb-,smk=8,xltvn=1,zdnzg=5,lm-,
sh=3,vtg-,xn-,lkp-,rqz-,xs-,bggff-,rzk=1,hr-,xs-,lnt-,rg-,pt-,drqq=5,bkc-,rvc=8,lnt-,td=3,rgkbzt=5,nxqhqd-,rgch-,
zcsc=6,xsbb=7,blmgvg-,dmv-,sxmq-,sf-,sgq=4,cdf-,vsjs=7,phd-,xzq-,rgqg-,hsm-,jrq-,pm=6,kb=3,pfs=5,klzj-,ls-,jzprfq-,
vndj=9,tss=8,ghdr-,skpq-,ntxqq=6,jz-,lmt=1,tl-,ptfs-,pt=9,qcr-,vkxm=2,mrd-,btp=3,lj-,llvv=5,qjn-,jr=6,gd=8,rsv=9,
clxz-,bvb=1,tnrm-,jrp=1,dj-,lj=7,dnc=4,cv-,tm=4,jtx=7,zx-,br-,njp=9,zrb-,hfdzfc-,hbd=1,kfjgqb=1,jz=3,jn-,dhh-,zx-,
hbq-,ng=2,dk=4,klzj=3,tss-,tm-,vsjs=6,vkk=7,hbd=4,jm=7,gj=7,ptmc=1,rmh-,lzs=8,qlnvt-,lgtd-,lqp=2,nfmf-,rgkbzt-,vqq-,
zjf-,kbl-,dvgz-,zjf-,kb-,pfxqhx=4,hdhk=8,xltvn-,qx-,fzx-,kcq-,hr-,gbzz=7,xjl=9,zsx-,bggff=2,hv=8,bkg-,krnq=8,sm-,
rl=6,mn-,bqm-,lkhb=3,lv-,lfz=7,ct-,pg=2,dqh=2,rx-,qx=1,mtqb=8,xv-,rq=1,tn-,dlrss-,gvf=8,mzpgh-,hr-,tshhq-,bkc-,fs=4,
glgpxh-,xll-,bkb-,tf=2,ztj-,zbl-,zcbg-,mjx-,hdhk=7,skpq-,flk-,kcx=2,mkv-,rgqg-,cz=4,hpc-,kczn-,bqql-,ht-,vkxm-,
cbnq=4,rcx=1,tz=4,gvf=4,hfdzfc=8,ndtc=7,glrt-,jc=3,jgh-,crd-,xpm-,bl-,kcx-,pg-,ddccc=1,drqq-,df-,gnvx=1,mn=9,kkz-,
vqq=4,cpbb=4,hbq-,lqp-,fs-,nc=5,fbrz=5,jx-,dgd-,ct=3,pxs-,hsm=7,grxx-,rxptm=8,bv=7,ntxqq=5,hdhk-,nfhb-,jgmsl=1,bpd-,
qm-,fcbzpl=4,ztj-,sg-,xpllk=7,dc-,dz-,gzsb-,qrlrxg=1,skj-,cg=1,vqqp=7,glms=3,pfxqhx=7,cv-,qtz=9,xpd-,kx=6,jh-,tl-,
qsj=1,rgkbzt=7,sg-,xf-,krnq=3,gdx-,cnk-,rcx-,cz=6,jktcpk=6,vsjs=4,hhn=2,gzp=9,nxqhqd=3,pptj=8,tz=6,mtqb-,jqhg=4,dnc-,
kf-,drkhc-,nc-,qcr-,lnt=6,lfz-,zjf-,sl=6,qq=1,txs-,xn=9,sns-,grxx=1,cjxb=9,tjjfm-,kczn-,kqggd=8,csnq-,dhh-,gddghs=7,
gt-,ztj-,mltm=8,hvhd=4,rf-,ztj=4,jqhg=9,ng=4,lnrjh=5,jz-,mhkbd=5,qfczq-,fshfd=3,ddccc-,rzk-,zp=2,kfsxsd=7,zvd-,
tjjfm-,bg=2,fzl-,jgmsl-,gbzz-,zqvb-,tz=7,mn-,rv=3,qnzlf=9,gd=4,zhc-,rd-,skk=8,pvh-,qjn-,qsj-,gjqmpc=9,bpt=4,bl=7,
fk=7,kjkbm-,srt=6,flk-,smr-,lqp=8,rbft-,qtql-,zcbg-,dvgz=7,vkd-,pvh-,lcvzfp-,njp-,pg=6,sv-,vlxv-,lgtd=3,mxq=9,llvv-,
mn-,dhh-,xn=7,lsx-,ck-,vlp=2,glgpxh-,kjkbm=1,qhh=2,cc-,fc=4,pzbsd=7,rl=7,cn-,rl=3,qx-,hpc-,xr=4,lqlh=1,pl-,vxcfp-,
pxs-,qm=6,lsd-,fzl=8,qjcfl=6,nbh-,xlc=1,skk=8,scp-,gmv=7,xm-,mtqb-,xb-,qn-,dk=7,bqm-,rvlv=5,jh=1,zj-,xf-,tnrm=7,
sxvv=7,chh=1,tnng=7,pl-,bfx=8,mprx-,tmpd=3,tg-,hcpdv-,vn-,jrq=3,bkg=9,xs-,bv=4,kcq-,rvl-,btp=9,mrd-,vjm=1,zqvb=2,
vdb-,tnrm-,pv=3,xlss=7,grxx-,jktcpk=7,hmd-,xx=1,pvh=5,pzbsd=1,rqz-,vtg-,pxs=4,rzk=4,skk-,xnp-,xsbb-,vsjs-,sxqh-,
rgqg-,pt=4,qnx-,dvzlc=5,fshfd-,glrt=3,nm-,dj=7,gmp=1,dk-,nxqhqd-,hzp=4,fvmf-,fg-,ls-,lsd=7,cnb=7,rgkbzt=4,hk=3,
vhrd=1,cnd-,dgd=3,hcpdv=5,jm=2,sh=5,dz=7,zbl-,gh-,rq-,vf-,dtg-,gmp=2,qz-,dlrss=3,lhj-,mhbdch=6,bkc-,hxfkx=8,lsx=9,
ck-,hj-,zk-,vn-,ltsb-,pfs=7,lnt-,nbh=4,bggff=3,zsx=6,kf-,gsk-,kkz=7,dj=7,rdzzjm=8,fd=8,tjjfm=1,vlxv=1,jc=9,kssg-,
tnng-,ht=5,fshfd-,rrx-,sr=5,sxmq-,bkg=2,bl=3,qfczq=9,tshhq-,ck=2,rxptm=7,sfrd=6,skj=3,hkd=6,tshhq=1,ltc=7,vn-,rm-,
xs-,rrx-,zlt-,tshhq=9,xx=9,mbzz-,kmx-,mjx=5,xcd=5,rgkbzt-,xdblmh-,jdf=4,phq-,ng=1,pj=2,rgkbzt-,ck=1,zrdk-,jnq-,
qtql=3,gd-,lbrn-,bdt-,dd-,ztj=8,zvd-,hkd=1,mm=5,dgd-,fvmf=3,fd=4,drqq-,tz-,jtx-,lbrn=1,gqsr-,lv=8,qhh-,cg=6,cnd=2,
fbrz=3,bf-,vlkx-,ksm=5,gsk=7,ltpsq=8,xlss-,zxkv=8,kgx=1,qjcfl=6,sns=7,xr-,zsx-,xpm-,dh=6,gmp-,ndq=9,cn-,xprp-,fbrz-,
pt-,pxk=4,bcpb=9,kcx=1,fn-,klzj=8,nc-,qq-,xhs=4,dvgz=3,bvb-,vtg-,dl-,lf=9,vt=7,bkc=2,sf-,krz=6,pptj=4,xlc=4,lj-,
zppn-,dnbql-,zpkc=5,drkhc=7,dgd-,pzbsd-,bqql=6,lqlh-,tnrm-,lkhb-,txs=6,jgmsl=4,qx=4,tnrm=6,nzn=4,kgv-,rlx-,ctdr-,
tg=5,blxq=4,sm-,vt-,bl=3,qfczq=2,hbd=5,sgq=6,kqggd-,pj-,tjjfm=6,stskm-,cbnq-,lvh-,vf=7,glgpxh-,sgq=6,cpbb-,fh-,nh-,
blxq-,vzrg-,ls=7,bzb=7,rvl-,gsk-,nzn=4,sgq-,cp=3,nh=9,clv-,nj-,fspkn=2,kf-,dt-,tmpd-,fcv-,gld-,tl-,vt=4,jnq-,rlx-,
ndtc=9,kbl-,tmpd-,lbq-,ltsb-,nbh-,dvgz=7,bdz-,ghdr=4,gn=5,bggff-,jnq=8,mzpgh-,jr-,lcvzfp=8,dbj=3,pt=3,nc-,mrd=7,hv=2,
vlxv=8,vnsgg-,np=2,cjxb=3,glrt=6,lnrjh=4,qjn-,xjl=7,mh=4,kf-,tcjp=3,gn=2,cn-,ndq-,rvl-,gcjgs=5,dt-,gt=2,qpqx-,hmd-,
dk=6,znp=1,bv-,zs=3,bst-,kssg-,jb=1,mzpgh=9,xln-,hfr=1,jj=7,tgm=9,xzljl-,hr=8,pxk-,rgrd-,rp=5,fz=4,sm=4,jdr=7,pr-,
ctdr=9,zhg=9,hmd=4,zpkc=2,mprx=6,lf=4,vkk-,hvk-,kj=6,grxx=2,hbq-,zrdk-,drnvhj=3,vjm-,pfs=7,hdr-,lbrn-,ttgzdn=4,hc-,
stskm-,zb=5,zvd-,nst=9,krnq=3,mh-,vkxm=5,cc-,lnb-,scd=4,bn=1,xpllk-,clxz-,klzj-,drnvhj-,gzsb-,lsd=9,rxptm=8,qqvmc-,
vn=2,glgpxh-,qsj=8,xx=1,gvf=8,gmv=1,psk=5,zcjnv-,mhkbd=2,mltm=2,lftk-,qq=8,lnrjh=8,zk=1,mbzz-,qcr-,jvp-,skj=2,hcpdv-,
vg=6,gkb-,qlnvt-,xln-,mhkbd=5,lf-,hvk-,rrx=5,kkz=2,ng=7,jx-,jh-,xj=1,xs=1,clv=3,skk-,sns=1,lfz-,bggff=3,ztj-,lcvzfp-,
gmp=4,gmp-,mtqb=7,bv-,nxz-,fzl=3,sxqh-,kt-,rrx=2,xsbb=2,tdnm=1,pfxqhx=8,nfmf-,jbd-,cnb-,jktcpk-,ld=9,lx-,phd-,br=1,
bkg=2,zrb-,dqh-,kfjgqb-,rqs-,rsv=7,zjf=8,pv=5,hvhd-,gmv=4,tss-,fd=6,vzrg=6,zdr=6,lnt-,cdf=3,tcjp-,kx=6,qn=6,kv=8,
skpq-,cdf-,pxs=1,lgtd-,llvv-,zhc-,jm=5,rm=8,lm=2,kjkbm=1,krz-,df-,tj-,rvl-,qnzlf=3,df-,fvmf=6,tmpd-,csnq-,lsx=7,
mhbdch-,lppg-,dsnd=4,hq=6,cjxb-,hk-,zrdk=4,dgd=9,kjzb-,llb=5,xll-,rp=7,fqmdgn=8,zxkv=9,tcjp-,lfz-,rp-,td=4,tshhq=9,
kgpnf=4,xsdlmd-,cn-,zcjnv-,rqs-,qnn-,tmpd-,rrn=7,zb-,xpllk=2,cqs-,nfmf=6,jvp-,dkvqm-,zhc=6,jgmsl-,lzcp-,nfpqv-,ncn-,
llvv=4,mxq-,qnx-,xll-,cnb-,phq=7,klzj-,fshfd-,lzs=4,vnt=1,cp=3,rgqg=3,kqggd=3,qnzlf=6,lbq-,mf-,vqq-,xll-,xs=3,
hcpdv=6,sns-,hbd=6,qqvmc-,mjjph-,cz=4,mmx=3,vkjr-,zcsc-,stskm=9,dl-,lfz-,kbl-,rxptm-,mbzz=4,tfx-,cnb=5,jktcpk-,jrp=2,
cnd=5,sfqnlm-,tkz=8,rgkbzt=2,zs=9,dnc-,bst-,tbdb=9,zhg-,zcsc-,mhv-,pm-,qnx-,jrp-,jvp-,qq=6,mqq-,ht-,vc=9,kgpnf-,
kmx=2,ht=5,bl-,rqs-,xr=5,rb=1,xhs=2,xf-,cnb-,pg-,rx=9,rx=1,mf-,dl-,hj-,vqqp=2,gmv=1,dr=2,rgqg-,qfczq-,bg-,fzl-,rcx=7,
xtct=6,gsk-,bl=6,zdr-,vzrg=7,cv-,kt-,txs=9,fzx=6,rv=8,xtgd-,kt-,jm-,rzk-,vlhhb=8,kqggd=2,clv=7,xx-,vnsgg-,jgh-,rzk-,
lzs-,xll-,fqmdgn=8,xlc=2,zk=9,qx=2,vsjs=2,xltvn=5,xpd=8,qlnvt-,dvx-,hvd=5,qlnvt=6,fqmdgn=4,dcc=1,kfsxsd=5,fz-,zhc=5,
np-,dk-,qcr-,rv-,lnt-,nd=2,nfmf=8,dlrss-,nh-,nxqhqd-,xpd-,fh-,vk=3,vxcfp=9,flk-,jdf-,ld-,qk=5,dt-,rdzzjm=8,fzx-,lsd-,
dmn-,nzn-,xtgd-,ld=7,dcc=9,rvc-,xhs=2,xb-,kj=9,lppg=5,tcjp-,kv=3,gqsr=6,sxmq-,nbh-,rsv-,flk-,gmv-,xtpn=8,gh-,vlp=2,
kczn-,bf=7,lqlh=3,mntr-,hj-,jvp=9,vxb-,vlhhb-,ppz-,qfczq-,rsv-,bfx=1,ng-,xll=5,pvh=3,tshhq-,vkjr=8,nj-,jvp-,gggk=7,
vjkrjg-,mhv=4,stskm=5,zpkc-,qz=2,qk-,znp=9,ptfs=8,fs-,hj=2,tz=3,hzp-,qp=7,xtct-,ss-,rxb=8,zjttq-,kb=9,td=4,pm=5,
jgmsl=2,dt-,lqp=3,rl=7,pv=3,rm-,brt=1,bvb=9,dbj=8,vtg-,pj=6,gcq-,mxq=4,xnp=4,qp-,kfsxsd-,jdf=1,sh=4,kcx=7,hfdzfc=5,
stskm=1,qnn-,xsbb-,dlrss=9,tshhq-,dhh=6,sxmq-,fzx=9,lvh-,df=8,vc=1,vc-,xj-,btp=5,qfv=7,fxz=1,bst-,xm-,jtx-,mltm=7,
rxb=2,scp-,nzn=2,xtct=5,kjzb-,mmx-,vpmmf-,hvd-,fn-,zhg=9,jnq-,xnp=5,vkjr=5,krz-,krnq=3,xzljl=6,xx-,bcpb=7,ltc=3,lfz-,
mntr=9,hcpdv-,vn-,fshfd=4,cc-,krnq=2,fxz-,xlss=6,rx=9,bf-,zp=7,xzq=4,qggz-,hmd-,xjl=2,zcsc=1,znp-,flk=5,rm=9,nc=1,
mntr=7,ltc-,gd-,rsv-,ltpsq-,bg-,vqqp-,zppn=6,bf=7,sgq=4,xx-,hxfkx=4,njp=9,dc=4,zjf=4,mhkbd-,kk=9,tj-,mntr-,rgrd=5,
gbzz=4,cbnq=3,jm=8,fcv-,qpqx-,krz=7,xb=1,ltsb-,jktcpk=8,kjzb=7,npghs-,tj-,kmjs=2,kv=7,pl-,rgrd-,kkz-,gld-,kt-,gt-,
xltvn-,vhrd-,ptfs=4,bqql-,vnsgg=7,rrx-,zsx-,kk-,kjzb=8,jc-,gzp=1,rkk-,sxvv=2,np=9,zqvb=1,lm=5,xpd-,dgd-,qtql=5,ld-,
xtpn-,mrd=1,jm-,lppg=5,zc-,bcfzn=4,phq=4,flk-,gggk-,sns=8,rzk-,xprp-,mbzz=3,lx-,xs-,smr=6,btp=8,xpllk=9,jc-,zx-,dc-,
vlhhb=3,ltc=4,rx=3,dbj=3,zhg-,tn-,mvl-,qfv=4,blxq=4,pcz=3,cnb-,kgv=1,lhj-,zs-,zc-,kjzb-,pt-,zx-,lkp=5,cnb=9,qlgv=4,
cz=4,nbh=4,rkk-,tnrm=5,gjqmpc=4,mm=5,vqq-,lsd-,tss=4,vkxm-,xm-,rxb-,glrt=9,xll=9,kjkbm-,vjmdx-,mpd-,mkv-,jc=6,vkxm-,
csqh-,smr-,ncn-,zdnzg=9,jvp-,zpkc-,dcc-,dj-,lkzhxs-,scp=8,dcc=6,rlx-,rp=2,tf-,dhh-,jb=6,ltc=1,kk=5,fshfd=5,zp=7,
xzljl-,ltc-,gvf-,tb-,jj=5,xv=3,flk=3,xx-,mhkbd-,tb-,cnd=6,lnk-,dc-,pcz=9,sv=8,rqz=4,kk=2,xpllk=2,xltvn-,lgtd-,hr=6,
pptj-,bv=9,rdzzjm-,gzp-,dr=4,vqqp=7,td=2,brt=3,xm=1,lv-,nfmf=5,ltsb=7,pfxqhx=2,kgpnf-,lm=2,lqlh=2,ct-,mprx=5,phd=1,
qk=7,hkd-,qfczq-,jgh=1,tjjfm=2,lnrjh=2,dz=3,gcjgs=1,dvzlc-,pq-,nst=4,rvlv=4,hcpdv-,kkz-,kczn-,gggk-,lf-,bzb=6,
tjjfm=2,zc=3,kt=6,bfx=1,tjjfm-,cnd=7,jb=4,dgd=4,gh-,lm-,jzprfq=4,td=4,fk-,pt=1,dmn=7,rgqg=5,rgrd=3,gbv-,xpm-,qtql=9,
fz-,bkg=4,mprx-,mrd=5,rp=1,kcq=4,xtct-,mhv-,dvgz-,zbl-,lnk=1,dj-,kkz-,kj=2,scd=6,cqs=3,ttgzdn=6,rgch=7,pl-,mqq-,
hdhk=7,lx=8,jbd=5,fk-,fz=8,fcbzpl=6,bs-,xtct-,dz-,drkhc-,fbrz-,tb=6,hvhd-,krnq=5,xm-,bggff-,gjqmpc=3,dsnd=3,rb=5,
phh=8,vc-,mcfh=9,ddccc=4,zj-,lppg-,mjjph=7,dqh=8,lbq-,np-,mpd-,pv=7,kmjs=1,rrn-,vkxm-,dn-,gjqmpc-,mh=9,dsnd=3,phd=4,
skpq=9,cv-,pxk=7,vlkx=7,rzl-,td-,kfjgqb=8,btp=3,bn-,jzprfq-,hxfkx=1,sxmq-,qlgv-,gmp-,mjx-,xnp=8,xprp-,zhg=3,sm-,qx=8,
zqvb-,vk=8,krnq-,zppn=8,kbl-,zhg=9,ltsb=3,flp=1,mqq=4,ztj=8,qz=2,tkz-,lvh=7,ptmc=7,gh=6,ss=9,hh=5,qnx-,fz=1,mltm-,
xtct-,phq-,qlgv-,td-,kx=7,lsx=8,hfdzfc-,qm=4,xzq=3,gbv=1,zdr=2,nxz-,glms-,cjxb-,dgd=8,jb-,vn=1,ks=2,rv-,qjcfl-,
qsjch=2,xsbb=7,fvmf=7,jktcpk-,jn=7,jgh-,jgmsl=2,xsm-,ztj-,lfz=5,xx=9,hdhk-,kjkbm-,vjm-,fvmf=9,bqm=6,sxqh-,lppg-,jr-,
vk=3,xzljl=6,fs-,rx=9,jbd=4,zcsc-,qq-,cpbb-,tm-,lv=3,jj-,tgm=9,hbsv=6,jktcpk=8,mtqb-,rm-,rp-,dcc=8,kcx-,rq-,xs=4,
phh-,cnk-,pvh-,rkk=4,fvmf-,bcfzn=3,hj-,fzx-,ptmc=6,xcd=6,lnrjh=7,bst=3,gggk=4,cdn-,tjjfm-,clxz=6,tnrm-,zj=7,dd=9,
hpc-,vxb-,rgqg=6,rbft=5,zsx=7,qn-,tkz-,jb=9,lbrn-,lnb=1,glms-,fxjc-,bg-,gmv=1,sb=8,cg=3,ptmc-,jz=6,fd-,gjqmpc=4,
vpmmf-,zdr-,ptmc=4,jb-,qhh-,tm-,vndj-,zcjnv=2,kmx=4,rzl-,dr=9,dnbql-,mmx=4,xlc=6,nfmf=7,gd=5,xlss-,fs=8,bqql-,fz=4,
zqvb-,lhj-,phh-,lnrjh=6,mhv=3,bcpb-,fbrz-,ls=6,xsdlmd-,rkk=9,fzl=5,mjjph-,pqjf=4,kf=2,hc=9,qggz=5,ztj=1,ss=7,pxk=4,
pq-,vpmmf-,zppn=3,lgtd=5,lkp=9,dc=2,rqs-,kbl-,qrlrxg=2,dsnd-,dvzlc-,bpd-,lbq-,rx=3,sb=4,ltsb-,krnq-,jbd=5,dc=6,mmx-,
xdblmh=9,dnbql=6,sm=5,xx=4,hdhk=4,smr-,hcpdv-,ddccc-,bv=4,jr=6,gcjgs=7,xtgd-,hzp-,kmjs=3,sxqh=4,bn=4,tnng-,crd=7,rv-,
lkp=1,bdz-,dn-,gt=5,rqz-,rdzzjm=7,hvd=2,xsbb=3,jtx=9,hdhk-,fz=1,mpd-,jktcpk-,jdr-,sv-,pptj-,tkz-,pg-,tb=1,xr-,lv=9,
mjjph=8,ld=6,hcpdv-,cg-,gn=4,dkvqm-,bqm=6,nc=7,mhbdch=6,tg-,xdblmh=9,bggff-,sxqh=6,pqjf=1,fzx-,bqm=5,lnt=5,vkd-,lnk-,
fspkn-,bdz=4,bfx-,lv=6,klzj=4,fs=7,vlkx=9,nst=6,cn=1,jm=7,vnsgg-,hj=8,dcc-,hr-,bst-,hr=2,zhc-,mzpgh=5,kk-,pj=4,btp=1,
gqsr-,qsj-,ld-,tz-,vlkx=4,hcpdv=3,cz-,zcbg-,cv=1,nfpqv-,lbq=9,kcx=6,xtct-,bqm-,dz=4,fzx-,gcq=6,vkjr=5,tjjfm-,lmt-,
rbft-,kczn=2,nfpqv=8,mkv=4,zvd-,xlc-,qqvmc=8,zppn=2,kf=3,jm=2,rxb-,lv=2,klzj=9,bv=6,mqq=2,xpllk-,sxmq-,npghs=6,
cjxb=8,phq-,qnx=7,lvh-,cnk-,chh-,dgd-,tj=3,jx-,ptfs=9,hzp-,gj=5,xlss-,bkb-,tm-,hkr=7,hc=4,fvmf-,xnp=3,kjzb-,dl-,kx=5,
qlnvt-,tj-,tfx=4,tf-,zs-,xpd=7,glms=4,lfz=3,tj=3,chh-,sxvv-,xpd=8,lsx-,bggff=6,qm=3,krnq-,qz-,rq=3,ck-,cnk=1,ptmc=7,
jrq-,mpd=7,lfz=8,bv-,ss-,nj=6,hc=3,hpc-,hkd=7,qk-,lppg-,ltsb=5,hdhk=7,qjcfl=7,bg-,fz=2,dz=6,skj-,hzrxt-,rvl=8,cg-,
gzp=7,jvp-,fg-,hkr-,qx-,xtpn-,ls=1,vjmdx=5,vlxv-,xpllk=7,zxkv=4,dz=3,bqm=2,nzn=3,rgkbzt=2,rmh-,dgd=7,gnvx-,rvlv=2,
vk=8,xpm=5,mvl-,vk-,drnvhj-,lj-,jr-,xjl-,gzp-,cbnq-,hfr-,csnq=5,pcz=4,bgv-,bst=9,fk=7,jx=4,cdf=3,mkv-,mbzz-,fs-,
xpd=9,hsm=5,mn=1,tgm=4,mxq=5,fcbzpl=6,vxb-,jj=8,ndtc=6,mntr=7,zp-,gqsr=5,gn-,zcsc-,pqjf=4,pzbsd=5,rcx-,mhbdch-,
fshfd-,vk-,gn-,mhv=4,zdr=5,tj=2,nj-,hr=2,tkz=7,pq=9,sv-,dqh=6,qcr=4,bdt=4,td-,fh-,kbl-,rvl=5,vf-,hvd-,xtct-,qlgv-,
rbft-,mjx=1,xltvn-,cqs=3,vzrg-,gqsr-,dmn=5,dkvqm-,rxptm=9,dd-,pcz-,nm-,mm=7,qggz-,bst=9,glms-,nxz-,nfhb=2,qjn=1,pq=8,
vkk-,tj-,dvx=1,jc-,psk=5,rsv-,qm-,mzpgh-,dxl-,lbrn-,cn=3,pxk-,xln=8,ghdr=4,ht-,blmgvg=9,zdr-,hfdzfc-,xnp=7,hr-,zc-,
csqh-,tf-,mbzz-,ct=1,zp=7,mh-,cn=8,ng=6,vqqp-,fn-,pxk=8,nst-,sb=5,krnq-,krz=5,tgm-,krz=3,pcz-,zcjnv-,fn=4,rvc=6,bn-,
jvp=9,rrn=8,ddd=8,tcjp-,fxjc=8,vkxm-,jrp=8,dz-,jq=7,qnx-,znl=4,nst=9,vn-,vnt=9,jz-,mhbdch-,hfr=9,bdt=1,vpmmf-,pq-,
jb-,znp-,rgqg=3,xqb=8,dvzlc-,rd-,rd-,hj=6,mvl=5,zxkv-,cdf-,dbj=4,rm-,ntxqq-,ksm-,lppg-,ptfs-,hj=5,nfpqv-,lj=2,fc=8,
jtx-,xsbb=4,vndj-,mn-,pnm-,fz=1,npghs-,sns=4,zj-,fzl=4,znl-,cnb-,tgm=5,rxb-,znp-,xdblmh=8,fn=1,rv=5,hp=9,rcx-,xlss=4,
fz=7,mcfh-,sxmq=7,mkv=2,rqs-,dmn-,mltm=1,dsnd-,jnq-,rx=8,dgd-,jrp-,kcx-,sfqnlm=8,hcpdv-,hvk=9,xll=9,ppz=6,bcfzn=8,
bl-,hkr-,tkz=4,qlnvt-,xm=1,dtg-,lcvzfp-,qqvmc=9,hq-,ht=7,zdr-,srt-,cn=2,rl=5,vkd-,phd=7,tnng=1,drqq=2,dhh-,hdhk=5,
tl=3,vv=7,hkr-,lcvzfp-,phq-,lqlh=7,tbdb-,mrd-,rkk=9,qnzlf-,np=4,xlss-,vdb=7,dvzlc=5,fcbzpl=5,vlp-,tshhq=7,kk-,fd=7,
cnd-,vxb-,pt=4,gj=7,rvl=1,dqh=4,gh=5,ptfs-,cdf-,nh-,scp-,zdr-,qn=5,fcbzpl-,zppn-,dnbql=5,rrx-,jrq=5,gggk=8,xtct=8,
hv=4,rrx-,mf=5,clxz=1,sl=9,vk=4,xv=6,hk-,brt=2,gmv=2,gld=2,llvv-,ss=2,kjkbm=5,dlrss-,cnk=3,pm-,hvhd=5,zb=6,jdr-,
rqs=1,dj-,sxmq=6,xn-,lzs-,bv=5,zvd=7,np-,gjqmpc-,xlc-,gcjgs=2,hskv=3,rvl-,kqggd-,srt=4,rrx=3,cz-,tl-,qq-,cnb-,zhc-,
chh-,dtg-,vzrg-,vc-,sxmq=1,cz=4,zx-,fc=9,hbd-,kv-,ndq=2,rgkbzt-,tbdb=7,ksm=8,xpm=1,mprx=2,kjkbm=4,ptfs-,sm-,lsd=9,
xf-,rzk-,ctdr-,kcq=4,gqsr=9,sxvv-,kk-,lbq=7,jh-,rdzzjm=6,xjl-,cdn=4,vndj-,kt-,zrdk-,xnp-,jb=4,vlxv-,jgh=9,gcq-,bqm-,
jr=3,qm=4,nst-,ltpsq=3,lv=1,bcpb-,xf=4,jjp-,qsjch-,kkz-,gn-,pr-,kczn-,hdhk-,dbj-,hr=3,xprp=2,hbd-,zdnzg=4,zj-,cn=1,
ntxqq=3,tss-,dqh-,zcsc-,hvd-,cg-,qz=7,lkhb-,gmv=1,pfxqhx-,gd-,fvmf=3,rsv=7,stskm-,mmx=5,gvf=2,mprx=4,qtql-,vtg=7,
bqm-,qjcfl=3,lbq-,qsjch=1,np=1,jj-,zlt-,psk-,pxk-,kqggd=8,gjqmpc=2,gsk=4,zcsc-,vpmmf=1,bdz=9,tj=4,lgtd-,ks-,bpd-,
smk-,tgm-,rgqg-,njp=1,lkhb=1,mltm=3,mmx-,qq-,zc=6,mpd=2,fzl-,xln-,fd-,qcr-,lnk=7,qqvmc=4,gn-,ct-,psk=5,sxvv-,bcpb=7,
mcfh=6,rd-,cnk-,lcvzfp=5,rdzzjm-,hq-,njp=4,qk=1,tl=7,sfrd=4,hkd-,xltvn=2,ht=4,zb=3,jm=8,skpq=7,vkxm=6,ltpsq=5,nj-,
fzl=4,vnsgg-,lgtd-,lm=3,lnrjh=8,lmt=3,bzb=7,lnt=2,jx=5,kjkbm-,np=8,qk-,kfsxsd=8,mprx=5,zppn-,krnq=9,hbd=5,zxkv-,xf=8,
jbd=9,drnvhj=2,rp-,krnq=2,fxjc=1,rvc-,gddghs-,gvf=3,rd=6,pcz=7,mm-,vnsgg-,ltc=9,rp=3,tbdb=5,jjp-,rdzzjm-,pv-,xj=2,
fcv=5,kx-,cjd-,grxx-,vlkx=4,nfhb-,xtgd=2,dh-,qk-,jnq-,dvx=2,bvb-,pxk=9,dqh-,cqs-,pr-,xqb=4,gcq=3,zc=8,nc-,qm-,fk=2,
rb=9,zrdk-,jx=3,flk=5,rgrd-,cnd=8,hxfkx=9,kmjs=9,cnb-,jn-,bdz=6,bcpb=8,cjxb-,sh-,krnq-,fxz-,kcx-,cx=1,gld=4,pzbsd-,
tkz=9,dj=3,phq=4,lj=3,kmx=1,jz-,xln-,rgqg=8,gcq-,gggk=1,bpd-,pvh-,fk=4,hsm-,zx-,zpkc-,qsj-,sv-,sv=9,ptfs=3,hpc-,vlp-,
cp=9,jj-,hkr=7,df-,rg-,nst=6,lsx=5,vpmmf-,fshfd-,fk=6,mbzz-,pxk-,vsjs-,sxvv-,zsx=2,fcbzpl=9,sxqh=2,rxptm=3,pt=9,sh-,
kkz-,mprx-,dl=8,srt-,pv-,ttgzdn-,ltsb-,qlgv=6,mprx-,jx-,qx-,kbl-,lkhb-,bf=4,ks-,ppz=4,rf=9,qjcfl-,bdz=3,sm-,jx=6,nj-,
cv=2,xcd=2,scp-,mhv=2,fshfd=1,kfjgqb-,jqhg=8,smr-,gld=4,pvh-,sxmq=8,lnb-,zs-,jvp=7,pfs-,lx=2,sr=1,hdr-,phd=3,gmv-,
jr-,ltsb=1,nj=3,xb-,pptj=5,kgv-,zcbg=5,npghs=2,lkp=9,pcz-,mntr-,kcx=4,pxk-,zppn-,kqggd=4,xsbb-,hcpdv=9,qlnvt=4,vv=6,
jn-,pnm-,rcx-,gjqmpc=7,mh-,nst-,bkg=3,zjttq-,krnq=9,kssg=7,xsdlmd-,lf-,hp-,mprx-,gvf-,rxptm=8,vsjs=2,pqc-,ptmc-,
fshfd-,bqm-,sl-,gd-,lkp-,pj-,rzl-,sxmq=9,lnrjh-,mhkbd-,kt=3,sb=1,kk-,llvv-,kcx=3,hskv-,rqz-,drqq=4,qfv=6,rkk-,drqq=5,
lppg-,rrx-,hsm=1,lcvzfp=3,gqsr-,crd=6,dgd=2,jrq=1,xsm=7,tjjfm-,nst-,dsnd-,ltc=5,pm-,rvlv=1,qnx-,qtql=9,vnsgg-,vqqp-,
xpm=3,kt=8,glrt=6,krz=3,vzrg=2,bqql=3,hhn=5,rvl=3,ghdr=6,rxb=6,rlx-,csqh=1,gmv-,dn=7,pfxqhx-,lgtd-,dh=8,nm=6,sl-,gd-,
vxb-,xhs=7,cz-,tn-,brt=7,ks-,cpbb=4,lppg=9,mvl=4,jq=8,rv=7,hskv=6,hdr=8,nfmf=7,tnrm-,lsd=6,pq=8,xv=4,gbzz=2,jrq-,
bgv=9,xzq=1,ck=6,zb-,hskv=3,rxptm=5,xprp-,gqsr=2,dj-,smk-,fk=2,ddd-,vqqp=6,gddghs-,qlnvt=8,scd-,xhs=9,lnt-,xzq-,jc=2,
qsjch=3,mprx=1,smk-,ddd-,zrb=5,jh-,klzj=4,mh-,mrd-,jgh=1,mh=3,br=5,fn=5,ztj=4,xs-,hkd=5,qfv-,krnq-,zj-,qp-,qlnvt=4,
fvmf-,lsx-,jr-,xsdlmd-,vf=8,pcz-,hr=5,vqqp=3,qlgv=4,qk-,lppg=8,qhh-,bdmrg-,lkzhxs-,llvv=1,smk-,gcjgs-,gmv-,qfczq-,
fshfd=3,smr-,gcjgs-,dbj-,hsm=7,ghdr-,qtql-,lcvzfp-,zbl=4,mzpgh=3,nj-,jdf-,nzn-,sg-,tb-,flk-,qcr-,rg-,xsbb-,drnvhj=4,
gzsb=4,dhh-,txs-,lhj=6,zk-,ndtc=8,rvlv-,xb=7,qnzlf-,rzl-,pptj-,qlnvt=1,rmh=4,llb=9,vpmmf-,rx-,rq-,gld-,sg=2,zhg=5,
td-,ztj=3,qfv=4,nzn-,bkc-,pfxqhx-,fspkn=5,drkhc=9,drkhc-,flk-,xsbb=5,kcq=1,bn-,gkb=3,dvgz-,kczn=7,ltsb-,fspkn=2,dvx-,
ck-,tn-,zrdk-,xnp-,pv=3,rgrd-,vzrg=6,kfsxsd=6,xnp=7,zqvb-,dnc-,ltpsq-,nxz=4,xx=7,gt=4,xs=8,hkd=2,qggz-,hvhd-,mvl-,
dsnd-,cnk-,gbzz-,kfsxsd=2,cnk-,lbrn=8,fvmf-,rm=6,sxmq=5,cdf-,qlgv=3,hkd=4,hsm=7,mm-,gjqmpc-,ndq-,np-,xsm-,ld=8,dhh-,
sh-,zcjnv-,cdf=5,ncn=1,ncn-,bkc=2,hc-,cc=2,rv=4,lqp=5,lcvzfp=7,qqvmc-,ghdr=9,bpt=7,bpd=8,cnd-,hmd=6,mn-,qsjch-,lftk-,
zqvb=3,gzsb=9,hq-,bl-,kfjgqb-,ndtc=5,vlp-,klzj=5,vxb-,hmd=2,xzljl=7,hmd-,flk=5,mkv-,dqh-,mhkbd=9,cc-,sxqh-,vxcfp=6,
hkr=5,cjd-,hvhd-,xll=6,kkz=8,smr=4,skpq=7,xdblmh=5,lm-,hp-,qtz-,krz-,bdt=3,gjqmpc=2,lf-,blmgvg-,hzp-,lqlh=2,qk-,
ghdr-,zvd=3,rrn-,vsjs-,gbzz-,ct-,vsjs=5,phh-,fh-,dk=5,ng-,vv=8,tf=5,np=6,nfpqv=9,jgmsl-,jx-,jvp-,rgch=7,sfrd=6,sgq=9,
bqm=3,qfv-,cz-,hc-,phh-,vqq=1,mcfh=9,bpt-,qfv-,jr=5,brt=2,jjp=7,tmpd=9,ltc-,hhn-,hdhk=4,zrb=6,fzl=7,xll=6,nd=2,sr-,
rdzzjm=9,jgmsl=7,qnn=9,ptfs=3,vjmdx=7,mm-,gzp-,vlp-,xlss-,vg=6,cg-,dmv=2,pqc-,kjkbm-,ht-,gggk=8,gn=3,ltc-,hsm=9,
bqql-,zxkv=5,ndtc-,rzk-,qk-,kgx-,zj=1,lj=4,tjjfm-,hpc=1,vxcfp=9,xlc-,vc=3,lm-,hk=3,tnng-,vnsgg-,xsbb-,gt=9,fzx=4,
vhrd-,mmx=6,kjzb-,qn=4,qjcfl=4,ltc=6,hc-,hbd=8,blmgvg-,zppn=8,dnc=7,xdblmh-,kgpnf-,cg=8,xj-,vkk=9,dhh=7,mqq-,zhg-,
xll=9,zrdk=6,ndtc=7,bkc=3,xcd=4,nzn=4,hdr=9,lmt=7,lppg=2,rb-,smr-,glgpxh-,cbnq-,zpkc-,gvf-,hhn=8,vtg=8,fvmf=8,
ddccc=1,bqm-,llvv=2,nc-,mjjph=2,rvc=1,vlp=5,qk=5,gt=7,tf-,qcr=1,lf=9,ctdr=6,mm-,mn-,xv=6,hkd=8,mhbdch=2,gld-,fn-,
dkvqm-,lsd=5,drqq=1,vlhhb=8,pj-,fs-,ck=8,lqlh-,hfdzfc-,lmt-,brt=1,lhj-,sb=7,jm=3,kjkbm-,rrn-,xjl=8,dt=3,xb-,mh-,
zbl=4,rzk-,xs=8,rvl=5,hzrxt=4,mprx-,llb-,cdn-,jdf=4,mvl-,sxqh-,mntr=7,xhs=9,hdhk-,bvb-,gddghs=5,xprp=8,xprp=9,vzrg=9,
kfsxsd=2,mjjph=8,vkxm=5,fc=4,cg-,pnm=3,csnq-,pg-,zpkc-,sm-,nj=8,nxz=5,vnsgg=6,pptj-,vtg-,lbq-,vnt-,njp=9,sr=9,vkxm-,
ltpsq-,lppg=3,zsx-,rd=9,jh=6,phq-,dqh=1,zx=2,kk-,mcfh=3,qpqx=4,sxmq=9,dkvqm-,cjxb-,mbzz=4,cx-,jtx=8,qnzlf=4,ptfs-,
lnt-,sxvv=1,rmh-,vjkrjg=6,lppg=1,zp-,skk-,hdr-,gggk=1,xprp-,ptfs=2,lmt-,qnzlf-,dlrss=8,rxb-,vjkrjg=1,pcz=1,drkhc-,
qtz-,mjx-,rlx=4,vf-,vc-,bkb=3,xjl=9,rmh-,xtpn-,phd-,xsdlmd=7,dsnd-,jdf=5,hkr-,kv=5,fs=5,ptfs-,vsjs-,lvh-,xprp=5,kkz-,
ct-,vlp-,hbq-,xtpn=6,jr=9,rcx=6,pcz=4,mf=9,rq=4,xsbb-,rcx=6,jnq=4,lv-,lfz=9,lnrjh=6,kk=4,tg-,sgq-,llb-,ndq-,xsdlmd=1,
bkb=7,vt=2,kbl=4,fcv-,kt-,dkvqm=6,nm-,lsd=4,pnm-,mn-,mjx=9,drqq=8,ck=3,cdf-,ntxqq-,qqvmc-,cnd-,dh=2,dvgz-,zx=3,xb-,
tjjfm=4,xdblmh=3,vt-,kjkbm=6,vjmdx=5,tgm-,fcv-,zj-,skj-"""

TEST_INPUT = """rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"""


class Lens:
    def __init__(self, definition: str):
        label, operation, value = re.match(r'([A-Za-z]+)([-=])(\d*)', definition).groups()
        self._label = label
        self._operation = operation
        self._value = int(value) if value else None

    def __hash__(self):
        return self.find_hash(self._label)

    @property
    def focal_length(self) -> int | None:
        return self._value

    @focal_length.setter
    def focal_length(self, value):
        self._value = value

    @property
    def operation(self) -> str:
        return self._operation

    @staticmethod
    def find_hash(input_: str) -> int:
        val = 0
        for x in map(ord, input_):
            val += x
            val *= 17
            val %= 256
        return val

    @property
    def label(self) -> str:
        return self._label

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.label == other.label


class HashMap:
    def __init__(self):
        self._dict = defaultdict(list[Lens])

    def update(self, lens: Lens):
        lhash = hash(lens)
        match lens.operation:
            case '-':
                for i, present in enumerate(self._dict[lhash]):
                    if lens == present:
                        self._dict[lhash].pop(i)
            case '=':
                for present in self._dict[lhash]:
                    if lens == present:
                        present.focal_length = lens.focal_length
                        return
                self._dict[lhash].append(lens)

    def value(self, index: int) -> int:
        val = 0
        for i, lens in enumerate(self._dict[index]):
            val += (index + 1) * (i + 1) * lens.focal_length
        return val


def solve(input_: str, part_2: bool = False) -> int:
    sequence = input_.replace('\n', '').split(',')
    if not part_2:
        return sum(map(Lens.find_hash, sequence))
    hashmap = HashMap()
    for lens in map(Lens, sequence):
        hashmap.update(lens)
    return sum(map(hashmap.value, range(256)))


if __name__ == '__main__':
    expected_1 = [(1320, [])]
    for idx, e in enumerate(expected_1):
        e_total, e_params = e
        start = time.time()
        assert (total := solve(TEST_INPUT, *e_params)) == e_total, f'Test {1} for part 1 failed! {total=} {e_total=}'
        print(f'Part 1: [test {idx}] {total} [elapsed time: {(time.time() - start) * 1000:.5f}ms]')
    start = time.time()
    total = solve(INPUT)
    print(f'Part 1: {total} [elapsed time: {(time.time() - start) * 1000:.5f}ms]')

    expected_2 = [(145, [True])]
    if expected_2:
        for idx, e in enumerate(expected_2):
            e_total, e_params = e
            start = time.time()
            assert (
                total := solve(TEST_INPUT, *e_params)
            ) == e_total, f'Test {1} for part 2 failed! {total=} {e_total=}'
            print(f'Part 2: [test {idx}] {total} [elapsed time: {(time.time() - start) * 1000:.5f}ms]')
        start = time.time()
        total = solve(INPUT, True)
        print(f'Part 2: {total} [elapsed time: {(time.time() - start) * 1000:.5f}ms]')
