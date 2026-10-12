from pathlib import Path
import json

ROOT=Path(__file__).resolve().parents[1]
source=next((ROOT/'versions').glob('*V51.5.2*.html'))
target=ROOT/'editions/dust-and-debt-v51.5.2-en-beta.html'
# The archived Chinese build stays byte-identical. This reviewed phrase bank localizes
# core player routes at runtime without changing the game's internal comparisons.
rows='''
尘土与债务|Dust & Debt
道路六向资源与地图入口修复|Six-way roads, resources & map-entry fix
可交互的黑橡木立体酒馆|Interactive 3D Black Oak Saloon
正在点亮黑橡木酒馆|Lighting the Black Oak Saloon
摆正椅背、点亮桌灯，并铺开羊绒地毯……|Straightening chairs, lighting lamps, and rolling out the rug…
拖动鼠标转动第一人称视线（左右 ±70°）· 双击复位 · 点击场景物件打开功能|Drag to look around (±70°) · Double-click to reset · Click objects to use them
门外的风把告示吹得啪啪作响，像三十一个坏主意同时要求被选中。|The wind rattles the notices outside like thirty-one bad ideas demanding attention.
今晚表演牌亮着，但报名费和摔伤都算你自己的。|Tonight's show is open, but the entry fee and bruises are yours.
今天还可向|Today you can ask
条行情消息 · 直接点击人物|more patrons for market news · Click a character
最近|Latest
个名字暂不回流|names are temporarily out of rotation
后排奖杯桌|Rear Trophy Table
枚|trophies
从淘金模式带回的物资可用于后续任务，并按日维护|Supplies brought home from Gold Rush can support later jobs and require daily upkeep
声音 收起|Audio Close
月 ·|Month ·
日 /|/ 
人 ·|people ·
首月最低还款|First minimum payment
最低还款|Minimum due
债务|Debt
现金|Cash
运气|Luck
弹药|Ammo
体力|Stamina
生命|Health
声望|Reputation
正常|Normal
简单|Easy
困难|Hard
残酷|Brutal
赏 金 告 示|WANTED POSTERS
赏金告示|Wanted Board
通缉名册|Wanted roster
赏金|Bounty
危险|Danger
情报|Intel
活捉奖励|Alive reward
击毙奖励|Dead reward
接受任务|Accept bounty
查看目标|Inspect target
目标|Target
本月账本|Monthly Ledger
账本|Ledger
还款|Repay
高利贷|Loan shark
黑橡木酒馆|Black Oak Saloon
灰石镇酒馆|Graystone Saloon
酒馆后门|Back Room
酒馆情报|Saloon Intel
布置酒馆|Decorate Saloon
角色 / 坐骑装饰|Character / Mount Style
远征装备|Expedition Gear
永夜模式|Endless Night
淘金模式|Gold Rush
普通追捕地图引擎|Shared frontier map
动态生死榜|Live outlaw board
人物辨认|Identify suspects
藏宝图|Treasure Map
偷窃攻防|Theft & defense
签字并进入|Sign & Enter
在主城签订生死状|Sign the expedition contract in town
地图、骑行、城镇、背包、天气与普通追捕完全共用。|The map, riding, towns, pack, weather, and standard bounty systems are shared.
地图会在你接近边缘时继续扩展，只有亲自返回出生主城才能结算。|The map expands near its edges. You must return to your starting town to bank the expedition.
基础入场费|Base entry fee
可在入场前额外购买|Before entering, you may also buy
救命只保住人物，不保住本次未结算的钱、宝石和装备。|The lifeline saves your character, but not unbanked cash, gems, or gear.
难度|Difficulty
新手|Rookie
地狱|Hell
预付|Prepay
不签|Decline
元|credits
救命契约|Lifeline Contract
返回酒馆|Return to Saloon
确认并回酒馆|Confirm & Return
进入主城 · 清点并结算|Enter Town · Settle Loot
进入主城|Enter Town
待结算|Unbanked
必须回主城|Must return to town
回家方向|Direction home
主城距离|Distance home
当前位置|Current Location
路线计划|Route Plan
没有规划目的地|No route planned
已抵达目的地|Destination reached
点击地块：自动骑行|Click a tile to auto-ride
道路疾驰|Road Sprint
扎营|Camp
背包|Pack
收起背包|Close Pack
随身物品、藏宝图与战利品|Items, Treasure Maps & Loot
随身物品|Items
战利品|Loot
干粮|Rations
立即使用|Use Now
当前线索|Current clue
正在追踪|Tracking
对应唯一宝藏|Linked to one unique treasure
待结算金币|Unbanked gold
宝石|Gems
物资|Supplies
边境小地图|Frontier Minimap
旅行记录|Travel Log
图例|Legend
道路|Road
平原|Plains
农场|Farm
丘陵|Hills
水域|Water
未知|Unknown
白天|Daylight
夜晚|Night
酷热|Heat
暴雨|Storm
从容骑行|Steady Ride
盗宝人动态|Treasure Hunter Activity
刚进入边境|New to the frontier
你 · 无名猎人|You · Nameless Hunter
选择头像|Select a portrait
误杀平民|Killing a civilian
开启全图视野|Reveal Full Map
关闭全图视野|Hide Full Map
关闭后门|Close Debug Panel
运行数值与测试工具|Runtime Test Tools
直接设定金钱|Set Cash
应用金钱修改|Apply Cash
赌场|Casino
黑桃赌场|Black Spade Casino
铜钉轮盘|Brass-Pin Roulette
响尾蛇骰盅|Rattlesnake Dice
九扇铜窗|Nine Brass Windows
半条命|Half a Life
四道赛马|Four-Lane Racing
边境交易所|Frontier Exchange
下注|Bet
离开赌场|Leave Casino
回到赌场大厅|Back to Casino
轮盘|Roulette
赛马|Horse Race
交易所|Exchange
行情大厅|Market Floor
我的持仓|My Holdings
多票走势对比|Compare Charts
查看涨跌与拥挤榜|Movers & Crowding
今日涨幅榜|Top Gainers
今日跌幅榜|Top Losers
最拥挤方向|Crowded Trades
今日没有新的大事故|No major incident today
边境快讯|Frontier News
等待新的资金方向|Awaiting market direction
行情日日换道，赢家只比别人早看见一步|Markets change trail daily; winners notice first
长角牧场联合|Longhorn Ranch Union
白桦牛奶社|White Birch Dairy
赤谷作物行|Red Valley Crops
牲口市场|Mount Market
马厩|Stable
繁育|Breeding
购买|Buy
出售|Sell
装备|Equip
坐骑|Mount
借来的马|Borrowed Horse
速度|Speed
耐力|Endurance
灵活|Agility
胆量|Courage
马主开价|Owner asks
冠军挂牌|Champion listing
回到赛马大厅|Race Hall
第一声马蹄属于你|The first hoofbeat is yours
赢下乡镇新秀赛|Wins the town maiden race
投入筹码|Wager
所得名次|Finish
赛后获得|Payout
净变化|Net
买下冠军|Buy Champion
回赌场|Back to Casino
选择一匹参赛马|Choose a Runner
开始比赛|Start Race
角色装饰|Character Style
坐骑装饰|Mount Style
保存装扮|Save Outfit
新档确认|New Game Confirmation
清除并重新开始|Erase & Restart
保留当前进度|Keep Current Progress
保存游戏|Save Game
读取游戏|Load Game
新游戏|New Game
导出存档|Export Save
导入存档|Import Save
读取并校验|Load & Verify
存档时间|Saved
读取失败|Load failed
存档校验失败|Save verification failed
开启声音|Enable Sound
声音：开|Sound: On
伴奏：开|Music: On
伴奏：关|Music: Off
音量|Volume
酒馆小曲待奏|Saloon music ready
荒野小曲待奏|Frontier music ready
回到大厅|Back to Hall
枪法|Gunplay
硬汉|Grit
口才|Charm
洞察|Insight
骑术|Riding
训练费|Training fee
能力牌|Skills
打听行情|Ask for news
酒馆客人|Saloon Patron
点击打听行情|Click for market intel
查看|Inspect
追捕归来|Back from the Hunt
远征|Expedition
准备|Prepare
出发|Depart
追捕|Hunt
地图|Map
决斗|Duel
开枪|Fire
对手|Opponent
回合|Round
命中|Hit
失手|Miss
中弹|Wounded
子弹擦着帽檐飞过|The bullet grazes your hat
强敌的子弹会造成更多伤害|A dangerous foe hits harder
任务失败|Mission Failed
任务完成|Bounty Complete
天气|Weather
补给|Supplies
线索|Clues
聚落|Settlements
探索|Exploration
地点|Locations
信息|Information
有效地点|Useful locations
情报等级|Intel level
还没有来自不同地点的可靠情报|No reliable intel from separate locations yet
引用证词|Cite Witness
封死退路|Block Escape
拆穿同伙|Expose Accomplice
利益交换|Make a Deal
徒步目标|Target on foot
目标体力|Target stamina
在聚落间活动|Moving between settlements
开启|Enable
关闭|Close
继续|Continue
离开|Leave
选择|Choose
费用|Cost
奖励|Reward
免费|Free
已拥有|Owned
未拥有|Not owned
成功|Success
失败|Failed
正在加载|Loading
请稍候|Please wait
分钟|min
小时|hr
普通|Standard
推荐|Recommended
确认|Confirm
取消|Cancel
返回|Back
第 1 天|Day 1
第 2 天|Day 2
第 3 天|Day 3
第 1 月|Month 1
第 2 月|Month 2
第 3 月|Month 3
'''
T=dict(line.split('|',1) for line in rows.strip().splitlines())
s=source.read_text(encoding='utf-8').replace('<html lang="zh-CN">','<html lang="en">',1)
s=s.replace('<title>尘土与债务 V51.5.2 · 道路六向资源与地图入口修复</title>','<title>Dust & Debt V51.5.2 · English Beta</title>',1)
payload=json.dumps(T,ensure_ascii=False,separators=(',',':'))
layer='''<style>#dd-enbar{position:fixed;right:14px;bottom:14px;z-index:99999;display:flex;gap:8px;align-items:center;padding:8px 10px;background:#241811ef;color:#f1d9aa;border:1px solid #b98a48;box-shadow:0 6px 24px #0008;font:700 11px/1.3 Georgia,serif}#dd-enbar a{color:#f3d790;text-decoration:none;border-left:1px solid #765537;padding-left:9px}#dd-enbar small{font:600 9px/1.3 system-ui;color:#c8ad82;max-width:220px}</style><div id="dd-enbar"><span>🌐 ENGLISH BETA</span><small>Core routes translated; rare event text may remain Chinese.</small><a href="../versions/尘土与债务_V51.5.2_道路六向资源与地图入口修复版.html">中文版 ↗</a></div><script>(()=>{const D=__D__,E=Object.entries(D).sort((a,b)=>b[0].length-a[0].length),S=new WeakMap(),tr=s=>{if(!s||!/[\\u3400-\\u9fff]/.test(s))return s;let o=s;for(const [z,e]of E)if(o.includes(z))o=o.split(z).join(e);return o},walk=r=>{if(r.nodeType===3){if(r.parentElement?.closest('#dd-enbar,script,style'))return;const o=S.get(r)??r.nodeValue;S.set(r,o);r.nodeValue=tr(o);return}if(r.nodeType!==1||r.matches('#dd-enbar,script,style'))return;for(const a of['title','aria-label','placeholder'])if(r.hasAttribute(a))r.setAttribute(a,tr(r.getAttribute(a)));for(const n of r.childNodes)walk(n)};let q=false;const run=()=>{q=false;walk(document.body);document.title='Dust & Debt V51.5.2 · English Beta'};new MutationObserver(()=>{if(!q){q=true;requestAnimationFrame(run)}}).observe(document.body,{childList:true,subtree:true,characterData:true,attributes:true,attributeFilter:['title','aria-label','placeholder']});run()})();</script>'''.replace('__D__',payload)
target.write_text(s.replace('</body>',layer+'\n</body>',1),encoding='utf-8')
print(f'Built {target.relative_to(ROOT)} with {len(T)} reviewed UI translations; original unchanged.')
