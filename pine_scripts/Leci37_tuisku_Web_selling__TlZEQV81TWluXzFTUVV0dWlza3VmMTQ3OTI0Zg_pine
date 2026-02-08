//Welcome to © Tuisku Trading Strategy, a sophisticated and optimised solution created by the experienced team at Tuisku.eu. Our team of experts specialise in random forest AI, harnessing its powerful capabilities to improve trading performance.
//Tuisku's commitment to quality and innovation shines through in every aspect of this strategy.


// Technical base pattern: Squeeze_Momentum_Indicator
// ID_model: NVDA_5Min_1SQU_f147924f Date Creation: 2024/10/18 Recommended expiry date : 2025/06/18
//@version=5
strategy("Tuisku_NVDA_5Min_1SQU_f147924f", overlay=true, margin_long=1000, margin_short=1000, pyramiding=1)
//RANDOM FOREST AI 
decision_tree_0_NVDA_5Min_f147924f(sqzOnInt, priceRange, lowerKC, lowerBB, rangema, noSqzInt, basis, val, ma, dev, sqzOffInt, upperBB, upperKC, avgHighLow)=>
	var float ret = 0  // # DecisionTreeRegressor(criterion=friedman_mse, max_depth=8, max_features=0.7,min_samples_leaf=4, min_samples_split=5,random_state=843828734)
	if( rangema <= 4.81299 )
		if( lowerKC <= 92.2542 )
			ret := 1.000000 // buy
		if( lowerKC > 92.2542 )
			if( val <= 0.005371 )
				if( upperBB <= 106.08 )
					if( rangema <= 0.546333 )
						if( lowerKC <= 98.6312 )
							if( upperKC <= 99.6291 )
								if( priceRange <= 0.725 )
									ret := 0.702703 // buy
								if( priceRange > 0.725 )
									ret := -0.500000
							if( upperKC > 99.6291 )
								if( ma <= 99.1568 )
									ret := -1.000000 // sell
								if( ma > 99.1568 )
									ret := -0.333333
						if( lowerKC > 98.6312 )
							if( lowerKC <= 103.791 )
								if( upperBB <= 102.846 )
									ret := 0.904110 // buy
								if( upperBB > 102.846 )
									ret := 0.639344
							if( lowerKC > 103.791 )
								if( rangema <= 0.475575 )
									ret := 0.167883
								if( rangema > 0.475575 )
									ret := 0.960000 // buy
					if( rangema > 0.546333 )
						if( ma <= 104.593 )
							if( lowerKC <= 101.753 )
								if( ma <= 97.6569 )
									ret := -0.888889 // sell
								if( ma > 97.6569 )
									ret := 0.303738
							if( lowerKC > 101.753 )
								if( lowerKC <= 102.245 )
									ret := -0.758621 // sell
								if( lowerKC > 102.245 )
									ret := 0.000000
						if( ma > 104.593 )
							if( val <= -0.002409 )
								if( lowerBB <= 104.325 )
									ret := 0.881356 // buy
								if( lowerBB > 104.325 )
									ret := -0.750000 // sell
							if( val > -0.002409 )
								ret := -0.714286 // sell
				if( upperBB > 106.08 )
					if( lowerKC <= 104.733 )
						if( upperBB <= 107.928 )
							if( basis <= 104.811 )
								if( upperKC <= 105.733 )
									ret := -0.200000
								if( upperKC > 105.733 )
									ret := 0.821429 // buy
							if( basis > 104.811 )
								if( rangema <= 0.647174 )
									ret := -0.685714
								if( rangema > 0.647174 )
									ret := -0.105882
						if( upperBB > 107.928 )
							if( lowerBB <= 98.2368 )
								ret := -0.500000
							if( lowerBB > 98.2368 )
								if( rangema <= 0.890321 )
									ret := -0.750000 // sell
								if( rangema > 0.890321 )
									ret := -1.000000 // sell
					if( lowerKC > 104.733 )
						if( avgHighLow <= 106.373 )
							if( rangema <= 0.218514 )
								if( avgHighLow <= 105.927 )
									ret := 0.000000
								if( avgHighLow > 105.927 )
									ret := -0.904762 // sell
							if( rangema > 0.218514 )
								if( upperBB <= 106.195 )
									ret := -0.240000
								if( upperBB > 106.195 )
									ret := 0.637615
						if( avgHighLow > 106.373 )
							if( lowerBB <= 108.573 )
								if( val <= -0.17364 )
									ret := 0.630435
								if( val > -0.17364 )
									ret := -0.189320
							if( lowerBB > 108.573 )
								if( ma <= 114.889 )
									ret := 0.243243
								if( ma > 114.889 )
									ret := 0.021618
			if( val > 0.005371 )
				if( upperBB <= 101.647 )
					if( lowerKC <= 97.6585 )
						if( ma <= 98.1123 )
							if( lowerKC <= 97.3105 )
								if( val <= 0.259026 )
									ret := -0.906250 // sell
								if( val > 0.259026 )
									ret := -0.071429
							if( lowerKC > 97.3105 )
								if( basis <= 97.9694 )
									ret := 0.500000
								if( basis > 97.9694 )
									ret := 0.000000
						if( ma > 98.1123 )
							ret := 1.000000 // buy
					if( lowerKC > 97.6585 )
						if( rangema <= 0.729962 )
							if( lowerBB <= 97.5192 )
								ret := 0.000000
							if( lowerBB > 97.5192 )
								if( dev <= 1.22728 )
									ret := -0.925532 // sell
								if( dev > 1.22728 )
									ret := -0.333333
						if( rangema > 0.729962 )
							if( lowerBB <= 98.8082 )
								ret := -0.750000 // sell
							if( lowerBB > 98.8082 )
								if( avgHighLow <= 100.035 )
									ret := 1.000000 // buy
								if( avgHighLow > 100.035 )
									ret := 0.142857
				if( upperBB > 101.647 )
					if( rangema <= 0.412224 )
						if( avgHighLow <= 106.597 )
							if( basis <= 105.183 )
								if( dev <= 0.538226 )
									ret := 0.444444
								if( dev > 0.538226 )
									ret := -0.348485
							if( basis > 105.183 )
								if( avgHighLow <= 105.371 )
									ret := 0.937500 // buy
								if( avgHighLow > 105.371 )
									ret := 0.475936
						if( avgHighLow > 106.597 )
							if( upperKC <= 107.522 )
								if( ma <= 106.807 )
									ret := -0.350000
								if( ma > 106.807 )
									ret := -0.696970
							if( upperKC > 107.522 )
								if( lowerBB <= 115.177 )
									ret := 0.294574
								if( lowerBB > 115.177 )
									ret := 0.122528
					if( rangema > 0.412224 )
						if( basis <= 278.597 )
							if( lowerKC <= 269.152 )
								if( avgHighLow <= 268.42 )
									ret := -0.032544
								if( avgHighLow > 268.42 )
									ret := 0.563025
							if( lowerKC > 269.152 )
								if( avgHighLow <= 272.937 )
									ret := -0.594937
								if( avgHighLow > 272.937 )
									ret := -0.155914
						if( basis > 278.597 )
							if( lowerBB <= 278.397 )
								if( priceRange <= 1.20378 )
									ret := 0.873016 // buy
								if( priceRange > 1.20378 )
									ret := 0.500000
							if( lowerBB > 278.397 )
								if( lowerBB <= 904.648 )
									ret := 0.071641
								if( lowerBB > 904.648 )
									ret := 0.180328
	if( rangema > 4.81299 )
		if( priceRange <= 7.05547 )
			if( lowerBB <= 782.421 )
				if( dev <= 5.93439 )
					if( val <= -0.922964 )
						ret := 1.000000 // buy
					if( val > -0.922964 )
						if( priceRange <= 4.59353 )
							if( val <= 0.371748 )
								if( rangema <= 5.04444 )
									ret := -0.666667
								if( rangema > 5.04444 )
									ret := -0.975610 // sell
							if( val > 0.371748 )
								if( rangema <= 5.0834 )
									ret := 0.750000 // buy
								if( rangema > 5.0834 )
									ret := -0.800000 // sell
						if( priceRange > 4.59353 )
							if( lowerBB <= 598.792 )
								ret := 0.250000
							if( lowerBB > 598.792 )
								ret := 0.750000 // buy
				if( dev > 5.93439 )
					if( rangema <= 6.55088 )
						if( dev <= 11.5899 )
							if( lowerBB <= 781.686 )
								if( dev <= 6.354 )
									ret := 0.000000
								if( dev > 6.354 )
									ret := 0.747664 // buy
							if( lowerBB > 781.686 )
								if( basis <= 792.793 )
									ret := -0.666667
								if( basis > 792.793 )
									ret := 1.000000 // buy
						if( dev > 11.5899 )
							if( dev <= 25.9424 )
								if( lowerKC <= 783.9 )
									ret := -0.383333
								if( lowerKC > 783.9 )
									ret := 0.777778 // buy
							if( dev > 25.9424 )
								if( lowerBB <= 455.561 )
									ret := 1.000000 // buy
								if( lowerBB > 455.561 )
									ret := 0.000000
					if( rangema > 6.55088 )
						if( dev <= 11.2861 )
							if( lowerBB <= 769.831 )
								if( upperBB <= 775.945 )
									ret := 0.166667
								if( upperBB > 775.945 )
									ret := 1.000000 // buy
							if( lowerBB > 769.831 )
								ret := -0.500000
						if( dev > 11.2861 )
							if( lowerBB <= 778.817 )
								if( val <= 1.74243 )
									ret := -0.528571
								if( val > 1.74243 )
									ret := 0.636364
							if( lowerBB > 778.817 )
								ret := 1.000000 // buy
			if( lowerBB > 782.421 )
				if( val <= -1.17506 )
					if( avgHighLow <= 907.591 )
						if( lowerKC <= 794.079 )
							ret := 1.000000 // buy
						if( lowerKC > 794.079 )
							if( dev <= 13.3386 )
								ret := 0.428571
							if( dev > 13.3386 )
								if( val <= -1.86649 )
									ret := -0.250000
								if( val > -1.86649 )
									ret := -1.000000 // sell
					if( avgHighLow > 907.591 )
						if( dev <= 11.1687 )
							ret := 0.000000
						if( dev > 11.1687 )
							if( upperBB <= 944.314 )
								if( upperKC <= 924.351 )
									ret := 1.000000 // buy
								if( upperKC > 924.351 )
									ret := 0.250000
							if( upperBB > 944.314 )
								ret := 1.000000 // buy
				if( val > -1.17506 )
					if( upperBB <= 843.774 )
						if( dev <= 16.7062 )
							if( lowerKC <= 785.336 )
								ret := -1.000000 // sell
							if( lowerKC > 785.336 )
								if( ma <= 795.707 )
									ret := 0.333333
								if( ma > 795.707 )
									ret := -0.779070 // sell
						if( dev > 16.7062 )
							ret := 1.000000 // buy
					if( upperBB > 843.774 )
						if( basis <= 834.139 )
							ret := 1.000000 // buy
						if( basis > 834.139 )
							if( basis <= 842.008 )
								if( sqzOnInt <= 0.5 )
									ret := -0.840000 // sell
								if( sqzOnInt > 0.5 )
									ret := 0.000000
							if( basis > 842.008 )
								if( upperKC <= 860.792 )
									ret := 0.206612
								if( upperKC > 860.792 )
									ret := -0.291556
		if( priceRange > 7.05547 )
			if( val <= -0.742278 )
				if( upperBB <= 1253.28 )
					if( upperBB <= 803.784 )
						if( basis <= 392.496 )
							ret := 0.750000 // buy
						if( basis > 392.496 )
							ret := 1.000000 // buy
					if( upperBB > 803.784 )
						if( priceRange <= 23.7799 )
							if( upperBB <= 1137.49 )
								if( upperBB <= 966.32 )
									ret := -0.250000
								if( upperBB > 966.32 )
									ret := -0.854167 // sell
							if( upperBB > 1137.49 )
								if( ma <= 1138.08 )
									ret := 0.250000
								if( ma > 1138.08 )
									ret := -1.000000 // sell
						if( priceRange > 23.7799 )
							ret := 1.000000 // buy
				if( upperBB > 1253.28 )
					if( priceRange <= 12.715 )
						ret := 0.500000
					if( priceRange > 12.715 )
						if( priceRange <= 18.7037 )
							ret := 1.000000 // buy
						if( priceRange > 18.7037 )
							ret := 0.750000 // buy
			if( val > -0.742278 )
				if( dev <= 4.61293 )
					ret := -1.000000 // sell
				if( dev > 4.61293 )
					if( upperBB <= 1231.34 )
						if( dev <= 32.6152 )
							if( ma <= 866.428 )
								if( ma <= 761.642 )
									ret := 1.000000 // buy
								if( ma > 761.642 )
									ret := 0.570248
							if( ma > 866.428 )
								if( upperBB <= 973.329 )
									ret := -0.080808
								if( upperBB > 973.329 )
									ret := 0.561224
						if( dev > 32.6152 )
							if( upperBB <= 742.625 )
								if( ma <= 518.859 )
									ret := 0.600000
								if( ma > 518.859 )
									ret := -1.000000 // sell
							if( upperBB > 742.625 )
								if( dev <= 36.5085 )
									ret := -0.250000
								if( dev > 36.5085 )
									ret := 0.750000 // buy
					if( upperBB > 1231.34 )
						if( val <= -0.11531 )
							ret := -0.750000 // sell
						if( val > -0.11531 )
							ret := -1.000000 // sell
	
    ret //return
// Define expected timeframe based on the selected interval: 5Min pine_value: 5   Trigger an alert and show a label if the timeframe is incorrect
alert_message_time_wrong = "The current candle TIMEframe is WRONG: "+ str.tostring(timeframe.period) + ", CHANGE it to the CORRECT one:  5MIN !!"
if (str.tostring(timeframe.period) != "5")
    alert(alert_message_time_wrong, alert.freq_once_per_bar_close)
    label.new(bar_index -300, high+30, text = alert_message_time_wrong, style = label.style_label_down,size = size.large, color = color.red, textcolor = color.white)
    log.error(alert_message_time_wrong)

//CODE associated with the technical indicator Squeeze_Momentum_Indicator 
//@version=5
//indicator "Squeeze Momentum Indicator [LazyBear]", shorttitle="SQZMOM_LB", overlay=false)

lengthBB = input.int(20, title="BB Length")
mult = input.float(2.0, title="BB MultFactor")
lengthKC = input.int(20, title="KC Length")
multKC = input.float(1.5, title="KC MultFactor")

useTrueRange = input(true, title="Use TrueRange (KC)")

// Calculate BB
source = close
basis = ta.sma(source, lengthBB)
dev = multKC * ta.stdev(source, lengthBB)
upperBB = basis + dev
lowerBB = basis - dev

// Calculate KC
ma = ta.sma(source, lengthKC)
priceRange = useTrueRange ? ta.tr(true) : (high - low)
rangema = ta.sma(priceRange, lengthKC)
upperKC = ma + rangema * multKC
lowerKC = ma - rangema * multKC

sqzOn = (lowerBB > lowerKC) and (upperBB < upperKC)
sqzOff = (lowerBB < lowerKC) and (upperBB > upperKC)
noSqz = not sqzOn and not sqzOff
sqzOnInt = sqzOn ? 1: 0   //Bool to int
sqzOffInt = sqzOff ? 1: 0   //Bool to int
noSqzInt = noSqz ? 1: 0   //Bool to int

avgHighLow = (ta.highest(high, lengthKC) + ta.lowest(low, lengthKC)) / 2
val = ta.linreg(source - (avgHighLow + ta.sma(close, lengthKC)) / 2, lengthKC, 0)

bcolor = val > 0 ? (val > nz(val[1]) ? color.lime : color.green) : (val < nz(val[1]) ? color.red : color.maroon)
scolor = noSqz ? color.blue : sqzOn ? color.black : color.gray

plot(val, color=bcolor, style=plot.style_histogram, linewidth=4)
plot(0, color=scolor, style=plot.style_cross, linewidth=2)


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
float op_operation = decision_tree_0_NVDA_5Min_f147924f(sqzOnInt, priceRange, lowerKC, lowerBB, rangema, noSqzInt, basis, val, ma, dev, sqzOffInt, upperBB, upperKC, avgHighLow)

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


