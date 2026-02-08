//Welcome to © Tuisku Trading Strategy, a sophisticated and optimised solution created by the experienced team at Tuisku.eu. Our team of experts specialise in random forest AI, harnessing its powerful capabilities to improve trading performance.
//Tuisku's commitment to quality and innovation shines through in every aspect of this strategy.


// Technical base pattern: Ultimate_MA_MTF_V2
// ID_model: ABNB_30Min_1ULT_3631913d Date Creation: 2024/10/18 Recommended expiry date : 2025/06/18
//@version=5
strategy("Tuisku_ABNB_30Min_1ULT_3631913d", overlay=true, margin_long=1000, margin_short=1000, pyramiding=1)
//RANDOM FOREST AI 
decision_tree_0_ABNB_30Min_3631913d(cr_up2Int, cr_downInt, avg2, avg, ma_downInt, cr_down2Int, cr_upInt, ma_upInt)=>
	var float ret = 0  // # DecisionTreeRegressor(criterion=friedman_mse, max_depth=6, max_features=0.9,min_samples_leaf=7, random_state=843828734)
	if( avg2 <= 115.379 )
		if( ma_upInt <= 0.5 )
			if( avg <= 104.82 )
				if( avg <= 96.608 )
					if( avg <= 95.432 )
						if( avg2 <= 95.7058 )
							ret := 0.134647
						if( avg2 > 95.7058 )
							ret := -0.311828
					if( avg > 95.432 )
						if( avg <= 95.9439 )
							ret := 0.700000 // buy
						if( avg > 95.9439 )
							ret := 0.369231
				if( avg > 96.608 )
					if( avg <= 97.579 )
						if( avg2 <= 98.8032 )
							ret := -0.466667
						if( avg2 > 98.8032 )
							ret := -0.953125 // sell
					if( avg > 97.579 )
						if( avg2 <= 103.784 )
							ret := -0.047131
						if( avg2 > 103.784 )
							ret := -0.512195
			if( avg > 104.82 )
				if( avg <= 106.686 )
					if( avg2 <= 108.956 )
						if( avg <= 106.021 )
							ret := 0.445783
						if( avg > 106.021 )
							ret := 0.702479 // buy
					if( avg2 > 108.956 )
						if( avg2 <= 110.622 )
							ret := -0.240000
						if( avg2 > 110.622 )
							ret := -0.533333
				if( avg > 106.686 )
					if( avg <= 113.266 )
						if( avg2 <= 107.018 )
							ret := -0.725806 // sell
						if( avg2 > 107.018 )
							ret := 0.085256
					if( avg > 113.266 )
						if( avg <= 114.787 )
							ret := 0.416031
						if( avg > 114.787 )
							ret := -0.078431
		if( ma_upInt > 0.5 )
			if( avg2 <= 87.8186 )
				if( avg2 <= 84.4032 )
					if( avg <= 84.7933 )
						if( avg <= 84.1614 )
							ret := 0.500000
						if( avg > 84.1614 )
							ret := 0.384615
					if( avg > 84.7933 )
						ret := 1.000000 // buy
				if( avg2 > 84.4032 )
					if( avg <= 84.9093 )
						if( avg2 <= 85.3509 )
							ret := 0.214286
						if( avg2 > 85.3509 )
							ret := 0.444444
					if( avg > 84.9093 )
						if( avg2 <= 85.15 )
							ret := -0.962264 // sell
						if( avg2 > 85.15 )
							ret := -0.200000
			if( avg2 > 87.8186 )
				if( avg2 <= 93.8926 )
					if( avg2 <= 92.7937 )
						if( avg <= 95.2465 )
							ret := 0.525490
						if( avg > 95.2465 )
							ret := -0.600000
					if( avg2 > 92.7937 )
						if( avg2 <= 93.4048 )
							ret := 0.932203 // buy
						if( avg2 > 93.4048 )
							ret := 0.654545
				if( avg2 > 93.8926 )
					if( avg <= 98.0871 )
						if( avg2 <= 94.6308 )
							ret := -0.727273 // sell
						if( avg2 > 94.6308 )
							ret := 0.186047
					if( avg > 98.0871 )
						if( avg <= 99.1172 )
							ret := 0.625000
						if( avg > 99.1172 )
							ret := 0.167123
	if( avg2 > 115.379 )
		if( avg <= 202.061 )
			if( avg2 <= 116.807 )
				if( avg <= 114.665 )
					if( avg <= 112.187 )
						ret := -1.000000 // sell
					if( avg > 112.187 )
						if( avg2 <= 115.529 )
							ret := -0.030303
						if( avg2 > 115.529 )
							ret := -0.563758
				if( avg > 114.665 )
					if( avg <= 115.678 )
						if( avg2 <= 116.606 )
							ret := 0.356021
						if( avg2 > 116.606 )
							ret := -0.400000
					if( avg > 115.678 )
						if( avg2 <= 116.357 )
							ret := -0.102484
						if( avg2 > 116.357 )
							ret := -0.377522
			if( avg2 > 116.807 )
				if( avg2 <= 117.498 )
					if( cr_upInt <= 0.5 )
						if( avg <= 118.7 )
							ret := 0.238095
						if( avg > 118.7 )
							ret := 0.759615 // buy
					if( cr_upInt > 0.5 )
						if( avg2 <= 117.167 )
							ret := -0.400000
						if( avg2 > 117.167 )
							ret := -0.642857
				if( avg2 > 117.498 )
					if( avg2 <= 147.783 )
						if( avg <= 121.784 )
							ret := -0.100644
						if( avg > 121.784 )
							ret := 0.048918
					if( avg2 > 147.783 )
						if( avg2 <= 150.292 )
							ret := -0.161773
						if( avg2 > 150.292 )
							ret := -0.033252
		if( avg > 202.061 )
			if( avg <= 202.617 )
				if( avg2 <= 200.111 )
					ret := -0.600000
				if( avg2 > 200.111 )
					if( avg2 <= 206.854 )
						if( avg <= 202.218 )
							ret := -0.888889 // sell
						if( avg > 202.218 )
							ret := -0.976190 // sell
					if( avg2 > 206.854 )
						ret := -0.700000 // sell
			if( avg > 202.617 )
				if( avg2 <= 198.341 )
					if( ma_upInt <= 0.5 )
						ret := -0.352941
					if( ma_upInt > 0.5 )
						if( avg <= 203.863 )
							ret := -1.000000 // sell
						if( avg > 203.863 )
							ret := -0.812500 // sell
				if( avg2 > 198.341 )
					if( avg2 <= 206.715 )
						if( avg <= 203.377 )
							ret := 0.586207
						if( avg > 203.377 )
							ret := 0.049296
					if( avg2 > 206.715 )
						if( avg <= 210.365 )
							ret := -0.661290
						if( avg > 210.365 )
							ret := -0.108527
	
    ret //return
// Define expected timeframe based on the selected interval: 30Min pine_value: 30   Trigger an alert and show a label if the timeframe is incorrect
alert_message_time_wrong = "The current candle TIMEframe is WRONG: "+ str.tostring(timeframe.period) + ", CHANGE it to the CORRECT one:  30MIN !!"
if (str.tostring(timeframe.period) != "30")
    alert(alert_message_time_wrong, alert.freq_once_per_bar_close)
    label.new(bar_index -300, high+30, text = alert_message_time_wrong, style = label.style_label_down,size = size.large, color = color.red, textcolor = color.white)
    log.error(alert_message_time_wrong)

//CODE associated with the technical indicator Ultimate_MA_MTF_V2 
//@version=5
//indicator title="CM_Ultimate_MA_MTF_V2", shorttitle="CM_Ultimate_MA_MTF_V2", overlay=true)

// Inputs
src = close
useCurrentRes = input(true, title="Use Current Chart Resolution?")
resCustom = input.timeframe(title="Use Different Timeframe? Uncheck Box Above", defval="D")
len = input.int(20, title="Moving Average Length - LookBack Period")
factorT3 = input.float(defval=7, title="Tilson T3 Factor - *.10 - so 7 = .7 etc.", minval=0)
atype = input.int(1, minval=1, maxval=8, title="1=SMA, 2=EMA, 3=WMA, 4=HullMA, 5=VWMA, 6=RMA, 7=TEMA, 8=Tilson T3")
spc = input(false, title="Show Price Crossing 1st Mov Avg - Highlight Bar?")
cc = input(true, title="Change Color Based On Direction?")
smoothe = input.int(2, minval=1, maxval=10, title="Color Smoothing - Setting 1 = No Smoothing")
doma2 = input(false, title="Optional 2nd Moving Average")
spc2 = input(false, title="Show Price Crossing 2nd Mov Avg?")
len2 = input.int(50, title="Moving Average Length - Optional 2nd MA")
sfactorT3 = input.float(defval=7, title="Tilson T3 Factor - *.10 - so 7 = .7 etc.", minval=0)
atype2 = input.int(1, minval=1, maxval=8, title="1=SMA, 2=EMA, 3=WMA, 4=HullMA, 5=VWMA, 6=RMA, 7=TEMA, 8=Tilson T3")
cc2 = input(true, title="Change Color Based On Direction 2nd MA?")
warn = input(false, title="***You Can Turn On The Show Dots Parameter Below Without Plotting 2nd MA to See Crosses***")
warn2 = input(false, title="***If Using Cross Feature W/O Plotting 2ndMA - Make Sure 2ndMA Parameters are Set Correctly***")
sd = input(false, title="Show Dots on Cross of Both MA's")

res = useCurrentRes ? timeframe.period : resCustom

// Hull MA definition
hullma = ta.wma(2 * ta.wma(src, len / 2) - ta.wma(src, len), math.round(math.sqrt(len)))

// TEMA definition
ema1 = ta.ema(src, len)
ema2 = ta.ema(ema1, len)
ema3 = ta.ema(ema2, len)
tema = 3 * (ema1 - ema2) + ema3

// Tilson T3 definition
factor = factorT3 * 0.10
gd(src, len, factor) => ta.ema(src, len) * (1 + factor) - ta.ema(ta.ema(src, len), len) * factor
t3(src, len, factor) => gd(gd(gd(src, len, factor), len, factor), len, factor)
tilT3 = t3(src, len, factor)

avg = atype == 1 ? ta.sma(src, len) : atype == 2 ? ta.ema(src, len) : atype == 3 ? ta.wma(src, len) : atype == 4 ? hullma : atype == 5 ? ta.vwma(src, len) : atype == 6 ? ta.rma(src, len) : atype == 7 ? tema : tilT3

// 2nd MA definitions
hullma2 = ta.wma(2 * ta.wma(src, len2 / 2) - ta.wma(src, len2), math.round(math.sqrt(len2)))
sema1 = ta.ema(src, len2)
sema2 = ta.ema(sema1, len2)
sema3 = ta.ema(sema2, len2)
stema = 3 * (sema1 - sema2) + sema3
sfactor = sfactorT3 * 0.10
sgd(src, len2, sfactor) => ta.ema(src, len2) * (1 + sfactor) - ta.ema(ta.ema(src, len2), len2) * sfactor
st3(src, len2, sfactor) => sgd(sgd(gd(src, len2, sfactor), len2, sfactor), len2, sfactor)
stilT3 = st3(src, len2, sfactor)

avg2 = atype2 == 1 ? ta.sma(src, len2) : atype2 == 2 ? ta.ema(src, len2) : atype2 == 3 ? ta.wma(src, len2) : atype2 == 4 ? hullma2 : atype2 == 5 ? ta.vwma(src, len2) : atype2 == 6 ? ta.rma(src, len2) : atype2 == 7 ? stema : stilT3

out1 = request.security(syminfo.tickerid, res, avg)
out2 = request.security(syminfo.tickerid, res, avg2)

// Formula for Price Crossing Moving Average #1
cr_up = open < out1 and close > out1
cr_down = open > out1 and close < out1

// Formula for Price Crossing Moving Average #2
cr_up2 = open < out2 and close > out2
cr_down2 = open > out2 and close < out2

// Barcolor Criteria for Price Crossing Moving Average #1
iscrossUp() => cr_up
iscrossDown() => cr_down

// Barcolor Criteria for Price Crossing Moving Average #2
iscrossUp2() => cr_up2
iscrossDown2() => cr_down2

ma_up = out1 >= ta.valuewhen(out1[smoothe] >= out1[1], out1[smoothe], 1)
ma_down = out1 < ta.valuewhen(out1[smoothe] < out1[1], out1[smoothe], 1)

col = cc ? (ma_up ? color.lime : ma_down ? color.red : color.aqua) : color.aqua
col2 = cc2 ? (ma_up ? color.lime : ma_down ? color.red : color.aqua) : color.white

plot(out1, title="Multi-Timeframe Moving Avg", linewidth=4, color=col)
plot(doma2 and out2 ? out2 : na, title="2nd Multi-TimeFrame Moving Average", linewidth=4, color=col2)
plot(sd and ta.crossover(out1, out2) ? out2 : na, style=plot.style_cross, linewidth=15, color=color.aqua)

// Barcolor Plot for Price Crossing Moving Average #1
barcolor(spc and iscrossUp() ? color.yellow : na)
barcolor(spc and iscrossDown() ? color.yellow : na)

// Barcolor Plot for Price Crossing Moving Average #2
barcolor(spc2 and iscrossUp2() ? color.yellow : na)
barcolor(spc2 and iscrossDown2() ? color.yellow : na)

cr_upInt = cr_up ? 1: 0    //Bool to int
cr_up2Int = cr_up2 ? 1: 0    //Bool to int
cr_downInt = cr_down ? 1: 0    //Bool to int
cr_down2Int = cr_down2 ? 1: 0    //Bool to int
ma_upInt = ma_up ? 1: 0    //Bool to int
ma_downInt = ma_down ? 1: 0    //Bool to int

// EXPLANATION OF THE STRATEGY
//The provided Pine Script implements a trading strategy that includes stop loss (SL) and multiple take profit (TP) levels,
//with an option to activate a trailing stop at the third TP level. Here's a detailed breakdown of its components and functionality:

//Variables Initialization:
var float stop = na
var float limit1 = na
var float limit2 = na

// Converts a percentage to points based on the average position price and the minimum tick size.
percent2points(percent) =>
    strategy.position_avg_price * percent / 100 / syminfo.mintick

// Stop Loss and Take Profit Inputs:
//Defines inputs for stop loss and three take profit levels in percentage terms.
sl = percent2points(input(2.92, title="stop loss %%"))
tp1 = percent2points(input(1.12, title="take profit 1 %%"))
tp2 = percent2points(input(2.31, title="take profit 2 %%"))
tp3 = percent2points(input(3.91, title="take profit 3 %%"))
activateTrailingOnThirdStep = input(false,title="activate trailing on third stage (tp3 is amount, tp2 is offset level)")
log.info("Stop Loss (sl):", sl," Take Profit 1 (tp1):", tp1, " Take Profit 2 (tp2):", tp2," Take Profit 3 (tp3):", tp3)

// Current Profit Calculation:
//Calculates the current profit in points based on the position size and price.
curProfitInPts() =>
    if strategy.position_size > 0
        (high - strategy.position_avg_price) / syminfo.mintick
    else if strategy.position_size < 0
        (strategy.position_avg_price - low) / syminfo.mintick
    else
        0
// Stop Loss and Profit Target Price Calculations:
//Determines the stop loss and profit target prices based on the position size and offset points.
calcStopLossPrice(OffsetPts) =>
    if strategy.position_size > 0
        strategy.position_avg_price - OffsetPts * syminfo.mintick
    else if strategy.position_size < 0
        strategy.position_avg_price + OffsetPts * syminfo.mintick
    else
        0
calcProfitTrgtPrice(OffsetPts) =>
    calcStopLossPrice(-OffsetPts)
// Current Stage Determination:
//Determines the current stage of the trade based on the profit points reached.
getCurrentStage() =>
    var stage = 0
    if strategy.position_size == 0
        stage := 0
    if stage == 0 and strategy.position_size != 0
        stage := 1
    else if stage == 1 and curProfitInPts() >= tp1
        stage := 2
    else if stage == 2 and curProfitInPts() >= tp2
        stage := 3
    stage
stopLevel = -1.
profitLevel = calcProfitTrgtPrice(tp3)

log.info("Stop Level:", stopLevel)
log.info("Profit Level:", profitLevel)
//This part of the strategy sets up exit conditions based on the current stage of the trade and uses the same exit ID "x" to modify the exit parameters dynamically.
//The exit parameters include stop loss, take profit, and comments for each stage.
// based on current stage set up exit
// note: we use same exit ids ("x") consciously, for MODIFY the exit's parameters
curStage = getCurrentStage()
float op_operation = decision_tree_0_ABNB_30Min_3631913d(cr_up2Int, cr_downInt, avg2, avg, ma_downInt, cr_down2Int, cr_upInt, ma_upInt)

log.info("Decision Tree Operation (op_operation):", op_operation)
if (op_operation <= 0)
    if curStage == 1
        stopLevel := calcStopLossPrice(sl)
        strategy.exit("x", loss = sl, profit = tp3, comment = "sl or tp3")
    else if curStage == 2
        stopLevel := calcStopLossPrice(0)
        strategy.exit("x", stop = stopLevel, profit = tp3, comment = "breakeven or tp3")
    else if curStage == 3
        stopLevel := calcStopLossPrice(-tp1)
        strategy.exit("x", stop = stopLevel, profit = tp3, comment = "tp1 or tp3")
    else
        strategy.cancel("x")


//SIGNAL MANAGE    User Adjustments and Risk Management
// The user can adjust the threshold values for op_operation to control the level of risk they are willing to take:
// Lower op_operation Threshold for Buy Signal (e.g., 0.5 instead of 0.55):
//     Effect: Generates more buy signals, increasing the frequency of trades. This is suitable for a user willing to take more risks and potentially capture more trading opportunities.
// Higher op_operation Threshold for Buy Signal (e.g., 0.8 instead of 0.55):
//     Effect: Generates fewer buy signals, reducing the frequency of trades. This is suitable for a user seeking to take fewer risks and only enter trades under more favorable conditions.
// Lower op_operation Threshold for Signal Closure (e.g., -0.8 instead of -0.9):
//     Effect: Closes positions less frequently, allowing trades more room to recover from temporary unfavorable conditions. This increases risk but can capture larger gains if the market reverses favorably.
// Higher op_operation Threshold for Signal Closure (e.g., -0.95 instead of -0.9):
//     Effect: Closes positions more frequently, exiting trades quickly at the first sign of unfavorable conditions. This decreases risk but may result in missed opportunities for recovery.
//Signal BUY
FIXED_DOLLAR_AMOUNT  = 10000
positionSize = FIXED_DOLLAR_AMOUNT / close
log.info("Position Size (in dollars $",FIXED_DOLLAR_AMOUNT,"):", positionSize)

if (op_operation >= 0.55)
    stop := close * 0.965
    limit1 := close * 1.03
    limit2 := close * 1.02
    strategy.entry("x", strategy.long, qty=positionSize, stop=stop, comment="in")
//Signal SELL
if (op_operation <= -0.9)
    strategy.close("x", comment = "under Le1")

// Impact on the Dataset
//Stop Loss (SL): Limits the maximum loss by exiting the position if the price moves against the trade by a specified percentage.
//Take Profit (TP1, TP2, TP3): Defines profit-taking levels to secure gains at different stages.
//Trailing Stop: Optionally activates a trailing stop at the third TP level to lock in profits while allowing for further gains if the price continues to move favorably.
//Position Entry and Exit: The strategy's buy and sell signals determine when to enter and exit positions, influencing the dataset by marking the points of trade execution and closure.
//Current Stage Tracking: Monitors the trade's progress through predefined stages, adjusting stop and profit levels accordingly.
//This strategy is designed to manage risk and maximize profits through a structured approach, incorporating multiple exit levels and dynamic adjustments based on market conditions. The dataset will reflect these actions, showing entries, exits, stop loss activations, and profit-taking events, providing valuable information for backtesting and performance analysis.
//Random forest AI offers significant advantages in trading, including the ability to handle large data sets, reduce overfitting and provide more robust predictions through the aggregation of multiple decision trees.

// NOTE: While the Tuisku team stands behind the quality and effectiveness of this trading strategy,
// PLEASE be aware that there is NO GUARANTEE of specific results or profits. TRADING INVOLVES SIGNIFICANT RISK, and it is important to use this strategy with careful consideration of your financial situation and risk tolerance.
// For further information and support, please contact us at Tuisku.eu.


