//Welcome to © Tuisku Trading Strategy, a sophisticated and optimised solution created by the experienced team at Tuisku.eu. Our team of experts specialise in random forest AI, harnessing its powerful capabilities to improve trading performance.
//Tuisku's commitment to quality and innovation shines through in every aspect of this strategy.


// Technical base pattern: Blai5_Koncorde_v10
// ID_model: LYFT_15Min_1KON_5eb4a31e Date Creation: 2024/10/18 Recommended expiry date : 2025/06/18
//@version=5
strategy("Tuisku_LYFT_15Min_1KON_5eb4a31e", overlay=true, margin_long=1000, margin_short=1000, pyramiding=1)
//RANDOM FOREST AI 
decision_tree_0_LYFT_15Min_5eb4a31e(verde_mean, verde, marron, media_azul, verde_media, nvi_ema, stoc, azul, verde_azul, pvi_ema, tprice, pvi, marron_mean, pvimax, azul_mean, xrsi, nvimin, media, source, oscp, nvim, xmf, pvimin, BollOsc, nvi, pvim, nvimax)=>
	var float ret = 0  // # DecisionTreeRegressor(criterion=friedman_mse, max_depth=7, max_features=0.5,min_samples_leaf=4, random_state=843828734)
	if( azul <= -58.7292 )
		if( oscp <= 18.2412 )
			if( nvi <= -0.811813 )
				if( xmf <= 39.4731 )
					if( pvimin <= 0.398748 )
						if( verde_mean <= -8.37165 )
							if( xrsi <= 18.9467 )
								ret := -0.733333 // sell
							if( xrsi > 18.9467 )
								ret := 0.827586 // buy
						if( verde_mean > -8.37165 )
							if( media_azul <= 151.356 )
								ret := -0.654676
							if( media_azul > 151.356 )
								ret := 0.375000
					if( pvimin > 0.398748 )
						if( verde_mean <= -17.9608 )
							if( verde_azul <= 29.4787 )
								ret := -0.060606
							if( verde_azul > 29.4787 )
								ret := 0.698630
						if( verde_mean > -17.9608 )
							if( media_azul <= 153.269 )
								ret := -0.180451
							if( media_azul > 153.269 )
								ret := 0.750000 // buy
				if( xmf > 39.4731 )
					if( nvimin <= -0.854253 )
						if( pvim <= 1.20186 )
							if( pvimin <= -0.116156 )
								ret := -0.120000
							if( pvimin > -0.116156 )
								ret := 0.587896
						if( pvim > 1.20186 )
							if( azul <= -89.0613 )
								ret := 0.200000
							if( azul > -89.0613 )
								ret := -0.625000
					if( nvimin > -0.854253 )
						if( tprice <= 49.1283 )
							if( pvimin <= 0.403632 )
								ret := 1.000000 // buy
							if( pvimin > 0.403632 )
								ret := -0.862069 // sell
						if( tprice > 49.1283 )
							ret := 1.000000 // buy
			if( nvi > -0.811813 )
				if( verde_media <= 19.5282 )
					if( verde <= 36.8298 )
						if( source <= 60.56 )
							if( marron <= -8.14064 )
								ret := 0.552632
							if( marron > -8.14064 )
								ret := 0.829670 // buy
						if( source > 60.56 )
							if( verde_media <= -55.4836 )
								ret := 0.250000
							if( verde_media > -55.4836 )
								ret := 0.000000
					if( verde > 36.8298 )
						if( xmf <= 58.3036 )
							if( verde_media <= -23.4792 )
								ret := 0.500000
							if( verde_media > -23.4792 )
								ret := -0.409091
						if( xmf > 58.3036 )
							if( verde <= 61.872 )
								ret := 0.333333
							if( verde > 61.872 )
								ret := 0.896552 // buy
				if( verde_media > 19.5282 )
					if( pvi <= 0.076864 )
						if( xmf <= 77.5805 )
							ret := 0.500000
						if( xmf > 77.5805 )
							ret := 0.000000
					if( pvi > 0.076864 )
						ret := -1.000000 // sell
		if( oscp > 18.2412 )
			if( marron_mean <= 90.6806 )
				if( verde <= 113.696 )
					if( marron_mean <= 29.9633 )
						if( xmf <= 48.686 )
							if( azul_mean <= -58.2062 )
								ret := 0.941176 // buy
							if( azul_mean > -58.2062 )
								ret := 0.000000
						if( xmf > 48.686 )
							ret := -0.500000
					if( marron_mean > 29.9633 )
						if( nvi_ema <= -1.26836 )
							if( source <= 14.1633 )
								ret := 0.645161
							if( source > 14.1633 )
								ret := -0.500000
						if( nvi_ema > -1.26836 )
							if( verde_mean <= 121.666 )
								ret := -0.426573
							if( verde_mean > 121.666 )
								ret := 0.666667
				if( verde > 113.696 )
					if( media <= 34.1249 )
						ret := 0.833333 // buy
					if( media > 34.1249 )
						if( verde_media <= 42.8576 )
							if( oscp <= 35.1234 )
								ret := -1.000000 // sell
							if( oscp > 35.1234 )
								ret := 1.000000 // buy
						if( verde_media > 42.8576 )
							if( source <= 10.85 )
								ret := 0.200000
							if( source > 10.85 )
								ret := -0.867647 // sell
			if( marron_mean > 90.6806 )
				if( azul_mean <= -47.0519 )
					if( nvimin <= -1.11617 )
						if( media_azul <= 158.013 )
							ret := 0.400000
						if( media_azul > 158.013 )
							if( BollOsc <= 31.7119 )
								ret := -1.000000 // sell
							if( BollOsc > 31.7119 )
								ret := -0.500000
					if( nvimin > -1.11617 )
						if( media <= 96.9519 )
							if( marron <= 86.5044 )
								ret := 0.500000
							if( marron > 86.5044 )
								ret := -0.125000
						if( media > 96.9519 )
							ret := 1.000000 // buy
				if( azul_mean > -47.0519 )
					if( pvimin <= 0.523835 )
						if( pvi <= -0.113659 )
							if( marron_mean <= 111.078 )
								ret := 0.250000
							if( marron_mean > 111.078 )
								ret := 0.000000
						if( pvi > -0.113659 )
							if( stoc <= 76.2439 )
								ret := 0.923077 // buy
							if( stoc > 76.2439 )
								ret := 0.642857
					if( pvimin > 0.523835 )
						if( verde_azul <= 192.022 )
							ret := -0.714286 // sell
						if( verde_azul > 192.022 )
							if( verde_mean <= 167.122 )
								ret := 0.750000 // buy
							if( verde_mean > 167.122 )
								ret := -0.200000
	if( azul > -58.7292 )
		if( media_azul <= 72.9998 )
			if( oscp <= 3.26574 )
				if( pvimin <= -0.411218 )
					if( media_azul <= 58.6745 )
						if( marron <= 34.9731 )
							if( azul_mean <= -18.3957 )
								ret := 0.250000
							if( azul_mean > -18.3957 )
								ret := 0.944954 // buy
						if( marron > 34.9731 )
							if( marron <= 73.4169 )
								ret := -0.043478
							if( marron > 73.4169 )
								ret := 0.891892 // buy
					if( media_azul > 58.6745 )
						if( azul <= -1.36959 )
							if( marron_mean <= 38.8491 )
								ret := -0.750000 // sell
							if( marron_mean > 38.8491 )
								ret := 0.866667 // buy
						if( azul > -1.36959 )
							if( BollOsc <= 3.16582 )
								ret := -0.750000 // sell
							if( BollOsc > 3.16582 )
								ret := -1.000000 // sell
				if( pvimin > -0.411218 )
					if( verde <= 87.8055 )
						if( media_azul <= 31.9127 )
							if( verde <= 21.1164 )
								ret := -0.011003
							if( verde > 21.1164 )
								ret := -0.104153
						if( media_azul > 31.9127 )
							if( pvimax <= -0.243889 )
								ret := -0.451220
							if( pvimax > -0.243889 )
								ret := 0.032884
					if( verde > 87.8055 )
						if( azul_mean <= 67.4478 )
							if( source <= 9.36287 )
								ret := 0.750000 // buy
							if( source > 9.36287 )
								ret := -0.219113
						if( azul_mean > 67.4478 )
							if( xrsi <= 66.3208 )
								ret := -0.166667
							if( xrsi > 66.3208 )
								ret := 0.626667
			if( oscp > 3.26574 )
				if( pvi_ema <= -0.337381 )
					if( nvi <= -0.999463 )
						ret := 1.000000 // buy
					if( nvi > -0.999463 )
						if( pvimax <= -0.361133 )
							if( source <= 19.48 )
								ret := -0.854167 // sell
							if( source > 19.48 )
								ret := -0.350000
						if( pvimax > -0.361133 )
							if( pvi_ema <= -0.451579 )
								ret := -0.750000 // sell
							if( pvi_ema > -0.451579 )
								ret := -1.000000 // sell
				if( pvi_ema > -0.337381 )
					if( azul_mean <= 23.7585 )
						if( source <= 10.2356 )
							if( marron_mean <= 79.9603 )
								ret := -0.024876
							if( marron_mean > 79.9603 )
								ret := 0.410377
						if( source > 10.2356 )
							if( pvi_ema <= 0.154287 )
								ret := -0.053703
							if( pvi_ema > 0.154287 )
								ret := -0.162237
					if( azul_mean > 23.7585 )
						if( nvimax <= -0.72217 )
							if( xrsi <= 88.2928 )
								ret := 0.076308
							if( xrsi > 88.2928 )
								ret := 0.764045 // buy
						if( nvimax > -0.72217 )
							if( verde_media <= 27.6377 )
								ret := 0.118881
							if( verde_media > 27.6377 )
								ret := -0.301538
		if( media_azul > 72.9998 )
			if( nvimin <= -0.916411 )
				if( verde_media <= 58.9844 )
					if( xrsi <= 85.5161 )
						if( marron_mean <= 106.468 )
							if( xmf <= 13.055 )
								ret := -0.211368
							if( xmf > 13.055 )
								ret := 0.092651
						if( marron_mean > 106.468 )
							if( azul <= 9.8326 )
								ret := 0.262241
							if( azul > 9.8326 )
								ret := 0.045408
					if( xrsi > 85.5161 )
						if( oscp <= 17.9546 )
							if( marron <= 119.03 )
								ret := -0.769231 // sell
							if( marron > 119.03 )
								ret := 0.304348
						if( oscp > 17.9546 )
							if( marron_mean <= 139.747 )
								ret := -0.632000
							if( marron_mean > 139.747 )
								ret := 0.500000
				if( verde_media > 58.9844 )
					if( verde <= 204.259 )
						if( oscp <= 30.025 )
							if( xmf <= 99.2841 )
								ret := -0.509091
							if( xmf > 99.2841 )
								ret := 0.625000
						if( oscp > 30.025 )
							if( nvimax <= -1.38786 )
								ret := 0.343137
							if( nvimax > -1.38786 )
								ret := -0.099676
					if( verde > 204.259 )
						if( azul <= 9.90757 )
							if( verde <= 359.362 )
								ret := 0.524793
							if( verde > 359.362 )
								ret := -0.875000 // sell
						if( azul > 9.90757 )
							if( marron <= 137.323 )
								ret := -0.761905 // sell
							if( marron > 137.323 )
								ret := 0.250000
			if( nvimin > -0.916411 )
				if( nvim <= -0.088546 )
					if( xrsi <= 83.3871 )
						if( stoc <= 74.506 )
							if( verde <= 91.571 )
								ret := -0.003060
							if( verde > 91.571 )
								ret := -0.181932
						if( stoc > 74.506 )
							if( pvimin <= 0.824389 )
								ret := 0.086304
							if( pvimin > 0.824389 )
								ret := -0.117261
					if( xrsi > 83.3871 )
						if( source <= 45.0856 )
							if( stoc <= 86.1796 )
								ret := 1.000000 // buy
							if( stoc > 86.1796 )
								ret := -0.318182
						if( source > 45.0856 )
							if( azul <= 24.2715 )
								ret := -0.756410 // sell
							if( azul > 24.2715 )
								ret := 0.000000
				if( nvim > -0.088546 )
					if( nvi <= -0.077408 )
						if( stoc <= 80.2426 )
							if( verde_azul <= 147.859 )
								ret := 1.000000 // buy
							if( verde_azul > 147.859 )
								ret := 0.842105 // buy
						if( stoc > 80.2426 )
							ret := 0.333333
					if( nvi > -0.077408 )
						if( nvi_ema <= -0.064473 )
							if( azul_mean <= -19.5641 )
								ret := 0.000000
							if( azul_mean > -19.5641 )
								ret := -0.250000
						if( nvi_ema > -0.064473 )
							ret := 0.250000
	
    ret //return
// Define expected timeframe based on the selected interval: 15Min pine_value: 15   Trigger an alert and show a label if the timeframe is incorrect
alert_message_time_wrong = "The current candle TIMEframe is WRONG: "+ str.tostring(timeframe.period) + ", CHANGE it to the CORRECT one:  15MIN !!"
if (str.tostring(timeframe.period) != "15")
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
float op_operation = decision_tree_0_LYFT_15Min_5eb4a31e(verde_mean, verde, marron, media_azul, verde_media, nvi_ema, stoc, azul, verde_azul, pvi_ema, tprice, pvi, marron_mean, pvimax, azul_mean, xrsi, nvimin, media, source, oscp, nvim, xmf, pvimin, BollOsc, nvi, pvim, nvimax)

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


