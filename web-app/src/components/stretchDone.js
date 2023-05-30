import styles from '@/styles/StretchDone.module.css'


const StretchDone = ({
    numSessions,
    breakSecondsLeft,
    skipTimer
}) => {

    return (
        <>
            <p>Number of sessions left: {numSessions}</p>
            <div className={styles.mainContainer}>
                <div className={styles.scoreCard}>
                    <h2>Well Done! Here is your final score:</h2>
                    <h1>120</h1>
                    <p>You have earned 12 points!</p>
                </div>
                <div className={styles.timerContainer}>
                    <h1>{Math.floor(breakSecondsLeft / 60)}:{(breakSecondsLeft - (Math.floor(breakSecondsLeft / 60) * 60) < 10) ? 0 : <></>}{breakSecondsLeft - (Math.floor(breakSecondsLeft / 60) * 60)}</h1>
                    <p>Left before break ends!</p>
                    <button className={styles.skipButton} onClick={()=>skipTimer("break")}>SKIP</button>
                </div>
            </div>

        </>
    );
}

export default StretchDone;