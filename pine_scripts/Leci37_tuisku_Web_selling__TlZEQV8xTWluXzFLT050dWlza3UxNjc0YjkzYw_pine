//Welcome to © Tuisku Trading Strategy, a sophisticated and optimised solution created by the experienced team at Tuisku.eu. Our team of experts specialise in random forest AI, harnessing its powerful capabilities to improve trading performance.
//Tuisku's commitment to quality and innovation shines through in every aspect of this strategy.


// Technical base pattern: Blai5_Koncorde_v10
// ID_model: NVDA_1Min_1KON_1674b93c Date Creation: 2024/10/18 Recommended expiry date : 2025/06/18
//@version=5
strategy("Tuisku_NVDA_1Min_1KON_1674b93c", overlay=true, margin_long=1000, margin_short=1000, pyramiding=1)
//RANDOM FOREST AI 
decision_tree_0_NVDA_1Min_1674b93c(verde_mean, verde, marron, media_azul, verde_media, nvi_ema, stoc, azul, verde_azul, pvi_ema, tprice, pvi, marron_mean, pvimax, azul_mean, xrsi, nvimin, media, source, oscp, nvim, xmf, pvimin, BollOsc, nvi, pvim, nvimax)=>
	var float ret = 0  // # DecisionTreeRegressor(criterion=friedman_mse, max_depth=7,max_features=sqrt, min_samples_leaf=4,random_state=843828734)
	if( nvimin <= -0.085468 )
		if( source <= 1239.13 )
			if( verde <= -22.6774 )
				if( pvim <= 0.499344 )
					if( verde_media <= -130.152 )
						if( verde_azul <= -308.334 )
							if( nvimin <= -0.087104 )
								ret := -0.928571 // sell
							if( nvimin > -0.087104 )
								ret := 0.666667
						if( verde_azul > -308.334 )
							if( verde_azul <= 7.65989 )
								ret := 0.794286 // buy
							if( verde_azul > 7.65989 )
								ret := -0.625000
					if( verde_media > -130.152 )
						if( marron_mean <= 0.552181 )
							if( nvimin <= -0.131829 )
								ret := 0.615584
							if( nvimin > -0.131829 )
								ret := 0.149533
						if( marron_mean > 0.552181 )
							if( xrsi <= 23.3799 )
								ret := -0.330909
							if( xrsi > 23.3799 )
								ret := 0.188781
				if( pvim > 0.499344 )
					if( BollOsc <= -47.4807 )
						if( media <= 42.3038 )
							if( nvim <= -0.149735 )
								ret := -0.758621 // sell
							if( nvim > -0.149735 )
								ret := 0.000000
						if( media > 42.3038 )
							if( BollOsc <= -61.7867 )
								ret := 0.666667
							if( BollOsc > -61.7867 )
								ret := 1.000000 // buy
					if( BollOsc > -47.4807 )
						if( pvim <= 0.517479 )
							ret := 1.000000 // buy
						if( pvim > 0.517479 )
							ret := 0.166667
			if( verde > -22.6774 )
				if( pvi <= 0.466169 )
					if( pvim <= 0.427903 )
						if( media <= 111.63 )
							if( pvimax <= 0.323681 )
								ret := 0.036118
							if( pvimax > 0.323681 )
								ret := 0.140756
						if( media > 111.63 )
							if( pvimax <= 0.314929 )
								ret := -0.004854
							if( pvimax > 0.314929 )
								ret := -0.600000
					if( pvim > 0.427903 )
						if( source <= 1122.3 )
							if( media <= 12.8777 )
								ret := 0.615385
							if( media > 12.8777 )
								ret := -0.808000 // sell
						if( source > 1122.3 )
							if( xrsi <= 41.3613 )
								ret := 0.187126
							if( xrsi > 41.3613 )
								ret := -0.089467
				if( pvi > 0.466169 )
					if( pvim <= 0.511853 )
						if( verde_media <= 24.4515 )
							if( nvimin <= -0.143588 )
								ret := 0.241821
							if( nvimin > -0.143588 )
								ret := 0.731707 // buy
						if( verde_media > 24.4515 )
							if( pvim <= 0.507191 )
								ret := -0.026667
							if( pvim > 0.507191 )
								ret := 0.383333
					if( pvim > 0.511853 )
						if( nvim <= -0.138797 )
							if( marron_mean <= 90.2554 )
								ret := -0.213362
							if( marron_mean > 90.2554 )
								ret := 0.297030
						if( nvim > -0.138797 )
							if( verde_azul <= 82.3224 )
								ret := 0.561983
							if( verde_azul > 82.3224 )
								ret := 0.164835
		if( source > 1239.13 )
			if( media_azul <= 85.9289 )
				if( nvi <= -0.156703 )
					if( azul <= -0.845004 )
						ret := 0.800000 // buy
					if( azul > -0.845004 )
						if( marron <= 73.107 )
							ret := -0.333333
						if( marron > 73.107 )
							ret := -0.250000
				if( nvi > -0.156703 )
					if( pvi <= 0.533354 )
						if( azul_mean <= 15.4722 )
							if( BollOsc <= -45.1658 )
								ret := -0.666667
							if( BollOsc > -45.1658 )
								ret := 0.095238
						if( azul_mean > 15.4722 )
							if( nvimax <= -0.133692 )
								ret := -0.551724
							if( nvimax > -0.133692 )
								ret := -1.000000 // sell
					if( pvi > 0.533354 )
						if( azul_mean <= 2.25688 )
							if( nvim <= -0.156544 )
								ret := -0.166667
							if( nvim > -0.156544 )
								ret := -0.923077 // sell
						if( azul_mean > 2.25688 )
							ret := -1.000000 // sell
			if( media_azul > 85.9289 )
				if( pvi <= 0.52927 )
					if( oscp <= 18.9241 )
						if( pvi_ema <= 0.523464 )
							ret := 0.222222
						if( pvi_ema > 0.523464 )
							ret := 1.000000 // buy
					if( oscp > 18.9241 )
						ret := -0.071429
				if( pvi > 0.52927 )
					if( oscp <= 8.84671 )
						ret := -0.500000
					if( oscp > 8.84671 )
						if( media <= 68.1231 )
							ret := 0.200000
						if( media > 68.1231 )
							if( oscp <= 18.9647 )
								ret := 0.000000
							if( oscp > 18.9647 )
								ret := -0.200000
	if( nvimin > -0.085468 )
		if( verde <= -22.9052 )
			if( azul <= -21.0296 )
				if( BollOsc <= -55.1767 )
					if( pvimin <= -0.862381 )
						if( xmf <= 33.616 )
							if( verde_azul <= -5.52434 )
								ret := 0.563559
							if( verde_azul > -5.52434 )
								ret := 0.180791
						if( xmf > 33.616 )
							if( verde_media <= -126.703 )
								ret := -0.781250 // sell
							if( verde_media > -126.703 )
								ret := 0.083333
					if( pvimin > -0.862381 )
						if( stoc <= 11.2252 )
							if( pvimax <= -0.411014 )
								ret := 0.154412
							if( pvimax > -0.411014 )
								ret := 0.826087 // buy
						if( stoc > 11.2252 )
							if( azul <= -154.334 )
								ret := 0.756098 // buy
							if( azul > -154.334 )
								ret := -0.161597
				if( BollOsc > -55.1767 )
					if( verde_mean <= -7.80209 )
						if( xrsi <= 16.9951 )
							if( azul <= -21.6828 )
								ret := 0.800000 // buy
							if( azul > -21.6828 )
								ret := -0.200000
						if( xrsi > 16.9951 )
							if( nvimin <= 0.887282 )
								ret := 0.395257
							if( nvimin > 0.887282 )
								ret := -0.857143 // sell
					if( verde_mean > -7.80209 )
						if( verde_mean <= 51.1274 )
							if( stoc <= 27.092 )
								ret := -0.166667
							if( stoc > 27.092 )
								ret := -0.961538 // sell
						if( verde_mean > 51.1274 )
							ret := 0.900000 // buy
			if( azul > -21.0296 )
				if( source <= 110.621 )
					if( source <= 99.4053 )
						if( media <= 14.1379 )
							if( azul_mean <= -21.6622 )
								ret := -0.692308
							if( azul_mean > -21.6622 )
								ret := 0.550000
						if( media > 14.1379 )
							if( marron <= -7.61947 )
								ret := 0.777778 // buy
							if( marron > -7.61947 )
								ret := -0.750000 // sell
					if( source > 99.4053 )
						if( azul_mean <= 25.4966 )
							if( verde_media <= -81.5419 )
								ret := 0.641860
							if( verde_media > -81.5419 )
								ret := 0.224540
						if( azul_mean > 25.4966 )
							if( nvimax <= 0.207226 )
								ret := 0.772727 // buy
							if( nvimax > 0.207226 )
								ret := -0.500000
				if( source > 110.621 )
					if( pvimin <= 0.077628 )
						if( nvi_ema <= -0.082032 )
							if( nvim <= -0.085107 )
								ret := -1.000000 // sell
							if( nvim > -0.085107 )
								ret := -0.600000
						if( nvi_ema > -0.082032 )
							if( media <= 18.1241 )
								ret := 0.062873
							if( media > 18.1241 )
								ret := -0.085287
					if( pvimin > 0.077628 )
						if( marron <= 13.656 )
							if( source <= 875.302 )
								ret := 0.830769 // buy
							if( source > 875.302 )
								ret := 0.142857
						if( marron > 13.656 )
							if( tprice <= 874.8 )
								ret := 0.000000
							if( tprice > 874.8 )
								ret := -0.800000 // sell
		if( verde > -22.9052 )
			if( marron_mean <= 49.1504 )
				if( BollOsc <= -37.3498 )
					if( media <= 4.96253 )
						if( azul <= -7.82078 )
							if( media_azul <= 33.4932 )
								ret := 0.149254
							if( media_azul > 33.4932 )
								ret := 0.753846 // buy
						if( azul > -7.82078 )
							if( pvi <= -0.527124 )
								ret := 0.883721 // buy
							if( pvi > -0.527124 )
								ret := -0.200000
					if( media > 4.96253 )
						if( verde <= 14.8903 )
							if( source <= 108.702 )
								ret := -0.113145
							if( source > 108.702 )
								ret := 0.027030
						if( verde > 14.8903 )
							if( oscp <= 2.65445 )
								ret := -0.280561
							if( oscp > 2.65445 )
								ret := 0.100000
				if( BollOsc > -37.3498 )
					if( verde_media <= -7.10313 )
						if( xmf <= 54.351 )
							if( azul_mean <= 70.8808 )
								ret := -0.080250
							if( azul_mean > 70.8808 )
								ret := 0.529412
						if( xmf > 54.351 )
							if( pvi_ema <= -0.722677 )
								ret := -0.145015
							if( pvi_ema > -0.722677 )
								ret := -0.649306
					if( verde_media > -7.10313 )
						if( marron <= 20.3461 )
							if( nvimax <= -0.064849 )
								ret := -0.886364 // sell
							if( nvimax > -0.064849 )
								ret := 0.297954
						if( marron > 20.3461 )
							if( verde_azul <= 34.987 )
								ret := 0.000912
							if( verde_azul > 34.987 )
								ret := -0.069010
			if( marron_mean > 49.1504 )
				if( oscp <= -11.8486 )
					if( tprice <= 828.087 )
						if( verde_mean <= 77.8209 )
							if( pvi <= -0.871605 )
								ret := 0.134322
							if( pvi > -0.871605 )
								ret := -0.069340
						if( verde_mean > 77.8209 )
							if( tprice <= 777.5 )
								ret := 0.202927
							if( tprice > 777.5 )
								ret := 0.967213 // buy
					if( tprice > 828.087 )
						if( nvi <= -0.012702 )
							if( pvim <= 0.010859 )
								ret := 0.945946 // buy
							if( pvim > 0.010859 )
								ret := 0.389313
						if( nvi > -0.012702 )
							if( pvimax <= -0.010006 )
								ret := 0.500000
							if( pvimax > -0.010006 )
								ret := -0.588235
				if( oscp > -11.8486 )
					if( media <= 120.917 )
						if( stoc <= 89.5291 )
							if( media_azul <= 123.868 )
								ret := -0.005428
							if( media_azul > 123.868 )
								ret := 0.172306
						if( stoc > 89.5291 )
							if( verde <= 121.184 )
								ret := 0.005279
							if( verde > 121.184 )
								ret := -0.155794
					if( media > 120.917 )
						if( source <= 120.488 )
							if( marron_mean <= 133.073 )
								ret := 0.892857 // buy
							if( marron_mean > 133.073 )
								ret := -0.050000
						if( source > 120.488 )
							if( nvim <= -0.03698 )
								ret := 0.545455
							if( nvim > -0.03698 )
								ret := -0.119658
	
    ret //return
// Define expected timeframe based on the selected interval: 1Min pine_value: 1   Trigger an alert and show a label if the timeframe is incorrect
alert_message_time_wrong = "The current candle TIMEframe is WRONG: "+ str.tostring(timeframe.period) + ", CHANGE it to the CORRECT one:  1MIN !!"
if (str.tostring(timeframe.period) != "1")
    alert(alert_message_time_wrong, alert.freq_once_per_bar_close)
    label.new(bar_index -300, high+30, text = alert_message_time_wrong, style = label.style_label_down,size = size.large, color = color.red, textcolor = color.white)
    log.error(alert_message_time_wrong)

//CODE associated with the technical indicator Blai5_Koncorde_v10 
//@version=5
//indicator title="Koncorde v10", shorttitle="Konk_v5", overlay=false)

// Declare variables with explicit types
var float pvi = na
var float nvi = na

tprice = ohlc4
lengthEMA = input.int(255, minval=1)
m = input.int(15)
source = hlc3

// Pececillos
pvi := volume > volume[1] ? nz(pvi[1]) + (close - close[1]) / close[1] : nz(pvi[1])
pvim = ta.ema(pvi, m)
pvimax = ta.highest(pvim, 90)
pvimin = ta.lowest(pvim, 90)
oscp = (pvi - pvim) * 100 / (pvimax - pvimin)

// Tiburones
nvi := volume < volume[1] ? nz(nvi[1]) + (close - close[1]) / close[1] : nz(nvi[1])
nvim = ta.ema(nvi, m)
nvimax = ta.highest(nvim, 90)
nvimin = ta.lowest(nvim, 90)
azul = (nvi - nvim) * 100 / (nvimax - nvimin)

// // Money Flow Index
// Money Flow Index
source_positive = ta.change(source) > 0 ? source : 0
source_negative = ta.change(source) < 0 ? source : 0
upper_s = math.sum(volume * source_positive, 14)
lower_s = math.sum(volume * source_negative, 14)
// Custom Money Flow Index calculation
money_flow_ratio = upper_s / lower_s
xmf = 100 - (100 / (1 + money_flow_ratio))


// Bollinger
mult = input.float(2.0)
basis = ta.sma(tprice, 25)
dev = mult * ta.stdev(tprice, 25)
upper = basis + dev
lower = basis - dev
OB1 = (upper + lower) / 2.0
OB2 = upper - lower
BollOsc = (tprice - OB1) / OB2 * 100

xrsi = ta.rsi(tprice, 14)

// Stochastic Calculation Function
calc_stoch(src, length, smoothFastD) =>
    ll = ta.lowest(low, length)
    hh = ta.highest(high, length)
    k = 100 * (src - ll) / (hh - ll)
    ta.sma(k, smoothFastD)

stoc = calc_stoch(tprice, 21, 3)
marron = (xrsi + xmf + BollOsc + stoc / 3) / 2
verde = marron + oscp
media = ta.ema(marron, m)
bandacero = 0.0

azul_mean = ta.sma(azul, 5)
verde_mean = ta.sma(verde, 5)
marron_mean = ta.sma(marron, 5)
verde_azul = verde - azul
verde_media = verde - media
media_azul = media - azul
media_marron = media - marron
pvi_ema = pvim
nvi_ema = nvi

// PLOT
vl = plot(verde, color=color.new(#66FF66, 0), style=plot.style_area, title="verde")  // GREEN
ml = plot(marron, color=color.new(#FFCC99, 0), style=plot.style_area, title="marron")  // BEIGE
al = plot(azul, color=color.new(#00FFFF, 0), style=plot.style_area, title="azul")  // CYAN
plot(marron, color=color.new(#330000, 0), style=plot.style_line, linewidth=2, title="lmarron")  // DARK RED
plot(verde, color=color.new(#006600, 0), style=plot.style_line, linewidth=2, title="lineav")  // DARK GREEN
plot(azul, color=color.new(#000066, 0), style=plot.style_line, title="lazul")  // DARK BLUE
plot(media, color=color.new(#FF0000, 0), title="media", style=plot.style_line, linewidth=2)  // RED
plot(bandacero, color=color.new(#000000, 0), title="cero")  // BLACK

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
float op_operation = decision_tree_0_NVDA_1Min_1674b93c(verde_mean, verde, marron, media_azul, verde_media, nvi_ema, stoc, azul, verde_azul, pvi_ema, tprice, pvi, marron_mean, pvimax, azul_mean, xrsi, nvimin, media, source, oscp, nvim, xmf, pvimin, BollOsc, nvi, pvim, nvimax)

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


