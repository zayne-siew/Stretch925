import BreakTime from '@/components/breakTime';
import Pomodoro from '@/components/pomodoro';
import styles from '@/styles/Timer.module.css'
import { useEffect, useState } from 'react';
import StretchIntro from './stretchIntro';
import StretchCam from './stretchCam';
import { IoMenu } from "react-icons/io5";
import StretchDone from './stretchDone';


const Timer = () => {
    const [isTimerActive, setIsTimerActive] = useState(false);
    const [originalSeconds, setOriginalSeconds] = useState(1500);
    const [secondsLeft, setSecondsLeft] = useState(1500);
    const [timer, setTimer] = useState();
    const [numSessions, setNumSessions] = useState(4);

    const [isBreak, setIsBreak] = useState(false);
    const [breakTimer, setBreakTimer] = useState();
    const [breakSecondsLeft, setBreakSecondsLeft] = useState(300);

    const [isStretch, setIsStretch] = useState(false);
    const [stretchView, setStretchView] = useState("intro")
    const [stretchTimer, setStretchTimer] = useState();
    const [stretchSecondsLeft, setStretchSecondsLeft] = useState(60);
    const [isStretchDone, setIsStretchDone] = useState(false);

    const startTimer = () => {
        setIsTimerActive(true);
        const timer = setInterval(() => {
            setSecondsLeft((secondsLeft) => secondsLeft - 1);
        }, 1000);
        setTimer(timer);
    };

    const stopTimer = () => {
        clearInterval(timer);
        setIsTimerActive(false);
        setSecondsLeft(originalSeconds);
        setNumSessions(4);
    }

    useEffect(() => {
        if (secondsLeft === 0 && numSessions != 0) {
            clearInterval(timer);
            setIsTimerActive(false);
            setSecondsLeft(originalSeconds);
            setNumSessions(numSessions - 1);
            setIsBreak(true);
            startBreakTimer();
        } else if (secondsLeft === 0 && numSessions === 0) {
            clearInterval(timer);
            setIsTimerActive(false);
            setSecondsLeft(originalSeconds);
            setNumSessions(4);
        }
    }, [secondsLeft, timer]);

    useEffect(() => {
        return () => clearInterval(timer);
    }, [timer]);

    const startBreakTimer = () => {
        const timer = setInterval(() => {
            setBreakSecondsLeft((breakSecondsLeft) => breakSecondsLeft - 1);
        }, 1000);
        setBreakTimer(timer);
    }

    useEffect(() => {
        if (breakSecondsLeft === 0) {
            clearInterval(breakTimer);
            setIsBreak(false);
            setBreakSecondsLeft(300);
            if (numSessions > 1) {
                startTimer();
            }
        }
    }, [breakSecondsLeft, breakTimer])

    const initStretch = () => {
        setIsStretch(true);
        setStretchView("intro");
    }

    const goToStretchView = () => {
        setStretchView("cam");
        startStretchTimer();
    }

    const goToDoneView = () => {
        setStretchView("done");
        setIsStretchDone(true);
        setIsStretch(false);

    }

    const startStretchTimer = () => {
        const timer = setInterval(() => {
            setStretchSecondsLeft((stretchSecondsLeft) => stretchSecondsLeft - 1);
        }, 1000);
        setStretchTimer(timer);
    }

    useEffect(() => {
        if (stretchSecondsLeft === 0) {
            clearInterval(stretchTimer);
            setStretchSecondsLeft(60);
            goToDoneView();
        }
    }, [stretchSecondsLeft, stretchTimer])


    return (
        <>
            <div className={styles.main}>
                <div className={styles.header}>
                    <div className={styles.headerMenu}>
                        <button className={styles.hamburgerMenuButton}>
                        <IoMenu />
                        </button>
                        <div className={styles.logo}>
                            <img src="../assets/logo.svg" alt="" />
                            <p>Stretch925</p>
                        </div>
                        <div className={styles.pointsBox}>
                            <p>My points: 88</p>
                        </div>
                    </div>

                    <div className={styles.divider}></div>
                </div>
                {
                    (!isBreak) ?
                        <Pomodoro {...{ isTimerActive, setIsTimerActive, secondsLeft, setSecondsLeft, startTimer, stopTimer, numSessions }} /> :
                        (isStretch) ?
                            <div className={styles.stretchViewContainer}>
                                {(stretchView === "intro") ? <StretchIntro {...{ numSessions, breakSecondsLeft, goToStretchView }} /> : <></>}
                                {(stretchView === "cam") ? <StretchCam {...{ numSessions, breakSecondsLeft, stretchSecondsLeft, goToDoneView }} /> : <></>}
                            </div>
                            :
                        (isStretchDone) ?
                            <StretchDone {...{numSessions, breakSecondsLeft,}}/>
                        :
                            <BreakTime {...{ numSessions, breakSecondsLeft, initStretch }} />

                }
            </div>
        </>
    );
}

export default Timer;