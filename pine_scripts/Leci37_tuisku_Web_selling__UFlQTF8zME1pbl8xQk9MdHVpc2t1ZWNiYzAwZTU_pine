//Welcome to © Tuisku Trading Strategy, a sophisticated and optimised solution created by the experienced team at Tuisku.eu. Our team of experts specialise in random forest AI, harnessing its powerful capabilities to improve trading performance.
//Tuisku's commitment to quality and innovation shines through in every aspect of this strategy.


// Technical base pattern: Bollinger_RSI_Double_Strategy
// ID_model: PYPL_30Min_1BOL_ecbc00e5 Date Creation: 2024/10/18 Recommended expiry date : 2025/06/18
//@version=5
strategy("Tuisku_PYPL_30Min_1BOL_ecbc00e5", overlay=true, margin_long=1000, margin_short=1000, pyramiding=1)
//RANDOM FOREST AI 
decision_tree_0_PYPL_30Min_ecbc00e5(crossunder_rsi_bbupperInt, BBlower, dif_source_BBupper, crossover_rsi_bblowerInt, vrsi, BBupper, dif_source_BBlower)=>
	var float ret = 0  // # DecisionTreeRegressor(max_depth=6, max_features=0.7, min_samples_split=10,random_state=843828734)
	if( vrsi <= 36.1425 )
		if( dif_source_BBupper <= -8.38344 )
			if( dif_source_BBupper <= -28.6875 )
				if( vrsi <= 15.2219 )
					if( BBlower <= 178.621 )
						if( dif_source_BBlower <= -5.34537 )
							ret := -0.210526
						if( dif_source_BBlower > -5.34537 )
							ret := 0.550000
					if( BBlower > 178.621 )
						if( dif_source_BBlower <= 4.34489 )
							ret := 0.727273 // buy
						if( dif_source_BBlower > 4.34489 )
							ret := -0.111111
				if( vrsi > 15.2219 )
					if( dif_source_BBlower <= 4.21421 )
						if( BBlower <= 238.077 )
							ret := 0.451807
						if( BBlower > 238.077 )
							ret := -0.164286
					if( dif_source_BBlower > 4.21421 )
						if( BBupper <= 181.789 )
							ret := 0.500000
						if( BBupper > 181.789 )
							ret := -0.300000
			if( dif_source_BBupper > -28.6875 )
				if( BBlower <= 81.496 )
					if( BBlower <= 70.8273 )
						if( vrsi <= 32.6026 )
							ret := -0.254826
						if( vrsi > 32.6026 )
							ret := 0.295082
					if( BBlower > 70.8273 )
						if( dif_source_BBlower <= -0.919377 )
							ret := 0.658824
						if( dif_source_BBlower > -0.919377 )
							ret := 0.075321
				if( BBlower > 81.496 )
					if( BBupper <= 95.4225 )
						if( dif_source_BBupper <= -11.5425 )
							ret := 0.075472
						if( dif_source_BBupper > -11.5425 )
							ret := -0.787709 // sell
					if( BBupper > 95.4225 )
						if( BBlower <= 84.483 )
							ret := 0.712766 // buy
						if( BBlower > 84.483 )
							ret := -0.055284
		if( dif_source_BBupper > -8.38344 )
			if( BBlower <= 187.419 )
				if( BBlower <= 182.242 )
					if( dif_source_BBupper <= -5.10237 )
						if( BBupper <= 73.8742 )
							ret := -0.026157
						if( BBupper > 73.8742 )
							ret := 0.201735
					if( dif_source_BBupper > -5.10237 )
						if( BBupper <= 61.606 )
							ret := 0.106142
						if( BBupper > 61.606 )
							ret := 0.026493
				if( BBlower > 182.242 )
					if( BBlower <= 183.094 )
						if( BBlower <= 182.617 )
							ret := -0.600000
						if( BBlower > 182.617 )
							ret := -0.904762 // sell
					if( BBlower > 183.094 )
						if( dif_source_BBlower <= 2.42247 )
							ret := -0.750000 // sell
						if( dif_source_BBlower > 2.42247 )
							ret := -0.092105
			if( BBlower > 187.419 )
				if( vrsi <= 35.2577 )
					if( BBupper <= 210.526 )
						if( BBlower <= 188.237 )
							ret := 0.333333
						if( BBlower > 188.237 )
							ret := 0.738739 // buy
					if( BBupper > 210.526 )
						if( dif_source_BBupper <= -7.9096 )
							ret := 0.523256
						if( dif_source_BBupper > -7.9096 )
							ret := 0.089307
				if( vrsi > 35.2577 )
					if( BBlower <= 271.083 )
						if( BBupper <= 266.763 )
							ret := -0.450000
						if( BBupper > 266.763 )
							ret := 0.600000
					if( BBlower > 271.083 )
						ret := -0.812500 // sell
	if( vrsi > 36.1425 )
		if( BBlower <= 76.0093 )
			if( BBupper <= 94.4357 )
				if( dif_source_BBupper <= -19.7003 )
					if( dif_source_BBlower <= 1.01644 )
						if( BBlower <= 75.2932 )
							ret := 0.976744 // buy
						if( BBlower > 75.2932 )
							ret := 0.000000
					if( dif_source_BBlower > 1.01644 )
						if( BBupper <= 93.8618 )
							ret := 1.000000 // buy
						if( BBupper > 93.8618 )
							ret := 0.100000
				if( dif_source_BBupper > -19.7003 )
					if( BBupper <= 37.1487 )
						if( dif_source_BBupper <= -0.567997 )
							ret := 0.122271
						if( dif_source_BBupper > -0.567997 )
							ret := 0.608434
					if( BBupper > 37.1487 )
						if( dif_source_BBupper <= -1.33362 )
							ret := 0.050938
						if( dif_source_BBupper > -1.33362 )
							ret := -0.029158
			if( BBupper > 94.4357 )
				if( dif_source_BBlower <= 0.84394 )
					ret := 1.000000 // buy
				if( dif_source_BBlower > 0.84394 )
					if( BBupper <= 98.2684 )
						if( BBlower <= 75.1705 )
							ret := -0.851064 // sell
						if( BBlower > 75.1705 )
							ret := -0.500000
					if( BBupper > 98.2684 )
						ret := 0.571429
		if( BBlower > 76.0093 )
			if( BBlower <= 112.158 )
				if( BBlower <= 107.732 )
					if( dif_source_BBlower <= 9.28537 )
						if( vrsi <= 64.4847 )
							ret := -0.012016
						if( vrsi > 64.4847 )
							ret := -0.109834
					if( dif_source_BBlower > 9.28537 )
						if( BBlower <= 82.1946 )
							ret := -0.582809
						if( BBlower > 82.1946 )
							ret := -0.142582
				if( BBlower > 107.732 )
					if( dif_source_BBupper <= -11.3763 )
						if( dif_source_BBupper <= -13.0326 )
							ret := -0.546875
						if( dif_source_BBupper > -13.0326 )
							ret := 0.729167 // buy
					if( dif_source_BBupper > -11.3763 )
						if( BBupper <= 120.435 )
							ret := -0.218023
						if( BBupper > 120.435 )
							ret := -0.535533
			if( BBlower > 112.158 )
				if( vrsi <= 86.0064 )
					if( dif_source_BBlower <= 23.2163 )
						if( BBlower <= 269.113 )
							ret := 0.006583
						if( BBlower > 269.113 )
							ret := -0.228052
					if( dif_source_BBlower > 23.2163 )
						if( BBlower <= 165.838 )
							ret := -0.211009
						if( BBlower > 165.838 )
							ret := 0.246454
				if( vrsi > 86.0064 )
					if( dif_source_BBlower <= 15.0525 )
						if( dif_source_BBupper <= -12.9196 )
							ret := -0.486381
						if( dif_source_BBupper > -12.9196 )
							ret := -0.231626
					if( dif_source_BBlower > 15.0525 )
						if( BBupper <= 301.836 )
							ret := -0.017682
						if( BBupper > 301.836 )
							ret := -0.833333 // sell
	
    ret //return
// Define expected timeframe based on the selected interval: 30Min pine_value: 30   Trigger an alert and show a label if the timeframe is incorrect
alert_message_time_wrong = "The current candle TIMEframe is WRONG: "+ str.tostring(timeframe.period) + ", CHANGE it to the CORRECT one:  30MIN !!"
if (str.tostring(timeframe.period) != "30")
    alert(alert_message_time_wrong, alert.freq_once_per_bar_close)
    label.new(bar_index -300, high+30, text = alert_message_time_wrong, style = label.style_label_down,size = size.large, color = color.red, textcolor = color.white)
    log.error(alert_message_time_wrong)

//CODE associated with the technical indicator Bollinger_RSI_Double_Strategy 
//@version=5
//strategy "Bollinger + RSI, Double Strategy (by ChartArt) v1.1", shorttitle="CA_-_RSI_Bol_Strat_1.1", overlay=true)

// ChartArt's RSI + Bollinger Bands, Double Strategy - Update
//
// Version 1.1
// Idea by ChartArt on January 18, 2015.
//
// This strategy uses the RSI indicator
// together with the Bollinger Bands
// to sell when the price is above the
// upper Bollinger Band (and to buy when
// this value is below the lower band).
//
// This simple strategy only triggers when
// both the RSI and the Bollinger Bands
// indicators are at the same time in
// a overbought or oversold condition.
//
// In this version 1.1 the strategy was
// both simplified for the user and
// made more successful in backtesting.
//
// List of my work:
// https://www.tradingview.com/u/ChartArt/
//
//  __             __  ___       __  ___
// /  ` |__|  /\  |__)  |   /\  |__)  |
// \__, |  | /~~\ |  \  |  /~~\ |  \  |
//
//

///////////// RSI
RSIlength = input.int(6, title="RSI Period Length")
RSIoverSold = 50
RSIoverBought = 50
price = close
vrsi = ta.rsi(price, RSIlength)

///////////// Bollinger Bands
BBlength = input.int(200, minval=1, title="Bollinger Period Length")
BBmult = 2 // input(2.0, minval=0.001, maxval=50,title="Bollinger Bands Standard Deviation")
BBbasis = ta.sma(price, BBlength)
BBdev = BBmult * ta.stdev(price, BBlength)
BBupper = BBbasis + BBdev
BBlower = BBbasis - BBdev
source = close
buyEntry = ta.crossover(source, BBlower)
sellEntry = ta.crossunder(source, BBupper)
plot(BBbasis, color=color.aqua, title="Bollinger Bands SMA Basis Line")
p1 = plot(BBupper, color=color.silver, title="Bollinger Bands Upper Line")
p2 = plot(BBlower, color=color.silver, title="Bollinger Bands Lower Line")
fill(p1, p2)

///////////// Colors
switch1 = input(true, title="Enable Bar Color?")
switch2 = input(true, title="Enable Background Color?")
TrendColor = (price[1] > BBupper and price < BBupper and BBbasis < BBbasis[1]) ? color.red : (price[1] < BBlower and price > BBlower and BBbasis > BBbasis[1]) ? color.green : na
// bgColor1 = color.new(TrendColor, 70)
barcolor(switch1 ? TrendColor : na)

// Using color.new() to set transparency
bgColor = color.new(TrendColor, 90)
bgcolor(switch2 ? bgColor : na)

///////////// RSI + Bollinger Bands Strategy
crossover_rsi_bblower = ta.crossover(vrsi, RSIoverSold) and ta.crossover(source, BBlower)
crossunder_rsi_bbupper = ta.crossunder(vrsi, RSIoverBought) and ta.crossunder(source, BBupper)

crossover_rsi_bblowerInt = crossover_rsi_bblower ? 1: 0    //Bool to int
crossunder_rsi_bbupperInt = crossunder_rsi_bbupper ? 1: 0  //Bool to int

dif_vrsi_RSIoverSold = vrsi - RSIoverSold
dif_source_BBlower = source - BBlower
dif_vrsi_RSIoverBought = vrsi - RSIoverBought
dif_source_BBupper = source - BBupper

// if not na(vrsi)
//     if crossover_rsi_bblower
//         strategy.entry("RSI_BB_L", strategy.long, stop=BBlower, oca_type=strategy.oca.cancel, comment="RSI_BB_L")
//     else
//         strategy.cancel(id="RSI_BB_L")
//
//     if crossunder_rsi_bbupper
//         strategy.entry("RSI_BB_S", strategy.short, stop=BBupper, oca_type=strategy.oca.cancel, comment="RSI_BB_S")
//     else
//         strategy.cancel(id="RSI_BB_S")

//plot(strategy.equity, title="equity", color=color.red, linewidth=2, style=plot.style_areabr)
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
float op_operation = decision_tree_0_PYPL_30Min_ecbc00e5(crossunder_rsi_bbupperInt, BBlower, dif_source_BBupper, crossover_rsi_bblowerInt, vrsi, BBupper, dif_source_BBlower)

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


